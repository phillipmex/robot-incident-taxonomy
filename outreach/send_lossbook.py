"""Lossbook outreach sender — Gmail compose via the VM's CDP Chrome (sanctioned
path), same pattern as aug/day02-g1-mailfix/send_g1.py. Reads data/staged/*.txt;
enforces the GLOBAL (cross-project) daily cap via aug/common/sendlog, since the
standing limit is <=50 cold emails/day across ALL projects, not just this one.
Run only after phill's explicit go-ahead per campaign-30/PLAYBOOK.md decision #9
("No cold email ever auto-sends without his go").

Usage: python send_lossbook.py [staged-file-name ...]   (no args = all staged)
"""
import glob
import json
import os
import re
import sys
import time
import urllib.parse

AUG_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "aug")
sys.path.insert(0, AUG_ROOT)
from common import sendlog
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
STAGED = os.path.join(BASE, "data", "staged")
ACCOUNT = "phillipmex@gmail.com"
CAMPAIGN = "lossbook-outreach"


def parse_staged(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    to = re.search(r"^To: (.+)$", text, re.M).group(1).strip()
    attach = re.search(r"^Attachment: (.+)$", text, re.M).group(1).strip()
    subject = re.search(r"^Subject: (.+)$", text, re.M).group(1).strip()
    body = text.split("Subject: " + subject, 1)[1].lstrip("\n")
    return {"file": os.path.basename(path), "to": to,
            "attachment": "" if attach == "(none)" else attach,
            "subject": subject, "body": body,
            "variant": os.path.basename(path)[0]}


def main():
    picks = sys.argv[1:]
    files = sorted(glob.glob(os.path.join(STAGED, "[A-Z]-*.txt")))
    if picks:
        files = [f for f in files if os.path.basename(f) in picks]
    targets = [parse_staged(f) for f in files]
    if not targets:
        print("nothing to send"); return
    if not sendlog.can_send(len(targets)):
        print(f"BLOCKED: {len(targets)} sends would exceed the global "
              f"{sendlog.GLOBAL_DAILY_CAP}/day cap ({sendlog.sent_today()} already sent)")
        return

    results = []
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        ctx = browser.contexts[0]
        for t in targets:
            r = {"file": t["file"], "to": t["to"], "status": "not-attempted"}
            page = ctx.new_page()
            try:
                params = urllib.parse.urlencode({
                    "authuser": ACCOUNT, "view": "cm", "fs": "1",
                    "to": t["to"], "su": t["subject"], "body": t["body"],
                })
                page.goto("https://mail.google.com/mail/?" + params, timeout=45000)
                page.wait_for_selector('input[name="subjectbox"]', timeout=30000)
                time.sleep(2)

                chip_ok = page.locator(f'[email="{t["to"]}"]').count() > 0 or \
                          page.locator(f'[data-hovercard-id="{t["to"]}"]').count() > 0
                subj = page.locator('input[name="subjectbox"]').input_value()
                body_ok = t["body"][:40].split("\n")[0] in page.locator('div[role="textbox"]').inner_text()
                if not chip_ok or subj != t["subject"] or not body_ok:
                    r["status"] = f"precheck-failed chip={chip_ok} subj={subj == t['subject']} body={body_ok}"
                    page.screenshot(path=os.path.join(STAGED, f"fail_{t['file']}_precheck.png"))
                    results.append(r); page.close(); continue

                if t["attachment"]:
                    if not os.path.exists(t["attachment"]):
                        r["status"] = "attachment-missing"
                        results.append(r); page.close(); continue
                    page.set_input_files('input[type="file"]', t["attachment"])
                    fname = os.path.basename(t["attachment"])
                    ok = False
                    for _ in range(30):
                        if page.locator(f'text="{fname}"').count() > 0:
                            ok = True; break
                        time.sleep(1)
                    if not ok:
                        r["status"] = "attachment-upload-unconfirmed"
                        page.screenshot(path=os.path.join(STAGED, f"fail_{t['file']}_attach.png"))
                        results.append(r); page.close(); continue
                    time.sleep(2)

                page.keyboard.press("Control+Enter")
                sent = False
                for _ in range(30):
                    content = page.inner_text("body") if not page.is_closed() else ""
                    if page.is_closed() or "Message sent" in content or "has been sent" in content:
                        sent = True; break
                    time.sleep(1)
                r["status"] = "SENT" if sent else "send-unconfirmed"
                if not sent:
                    page.screenshot(path=os.path.join(STAGED, f"fail_{t['file']}_send.png"))
            except Exception as e:
                r["status"] = f"error: {e}"
                try: page.screenshot(path=os.path.join(STAGED, f"fail_{t['file']}_exc.png"))
                except Exception: pass
            finally:
                try:
                    if not page.is_closed(): page.close()
                except Exception: pass
            results.append(r)
            if r["status"] == "SENT":
                sendlog.log(CAMPAIGN, t["to"], t["variant"], t["subject"], "sent",
                            note=t["file"])
            print(json.dumps(r, ensure_ascii=False), flush=True)
            time.sleep(8)

    out = os.path.join(STAGED, "send_results.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    sent_n = sum(1 for x in results if x["status"] == "SENT")
    print(f"DONE {sent_n}/{len(results)} sent -> {out}")


if __name__ == "__main__":
    main()
