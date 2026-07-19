# Evidence Pack Checklist — v0.1 DRAFT

**The "one-click evidence pack" concept, as a manual checklist.**

When a robot incident turns into a claim, the deployer typically faces three parallel documentation demands: the **OEM warranty claim**, the **RaaS/integrator SLA claim** (credits, remedy obligations), and the **insurance claim** (liability, property, or business-interruption). Each asks for overlapping but differently-framed evidence, and the evidence that decides them — logs, CCTV, scene photos — is the evidence that disappears fastest. This checklist is what a future Lossbook product would assemble automatically; today it is the standard for doing it by hand.

Companion: field codes reference `robot-incident-taxonomy-v0.1.md` (RIT v0.1).

---

## 0. Time-critical actions (first 24 hours)

These decay fastest; do them before any paperwork.

- [ ] **Preserve the scene state** (EV-08): photograph before cleanup/reset; record the time of first robot reset or power cycle.
- [ ] **Export robot + fleet-manager logs** (EV-02) covering at least 30 minutes pre-incident; keep the raw export, not a screenshot. Note: some RaaS platforms overwrite or age out logs — request a vendor-side preservation hold in writing the same day.
- [ ] **Pull video** (EV-03): robot cameras and site CCTV. CCTV retention is commonly 7–30 days (TO VERIFY per site) — export immediately.
- [ ] **Photograph everything** (EV-01): damage, robot position, sensor surfaces (occlusion/dirt), floor/environment condition, any injuries (with consent).
- [ ] **Capture witness details** (EV-04): names, roles, contacts; contemporaneous notes now, signed statements within days.
- [ ] **Record the software state** (EV-06): firmware, autonomy stack, map version, date of last update — before any vendor remote session can change it.
- [ ] **Document environmental conditions** (EV-07): lighting, floor state, weather, temporary obstructions.
- [ ] If anyone was injured: complete the site's injury/first-aid register entry and check jurisdictional reporting duties (e.g. OSHA recordability in the US — TO VERIFY thresholds per jurisdiction).

## 1. File the RIT record

- [ ] Create the incident record per RIT v0.1 (all required fields; `record_status: open` is fine — update as the investigation matures).
- [ ] Code parties inclusively (PT field) — you do not yet know which claim path will matter.
- [ ] Code near-misses too (HT-00): they cost nothing to file and are the leading-indicator data that makes later insurance conversations easier.

## 2. Warranty claim pack (against the OEM — PT-02)

What OEM warranty processes typically require. TO VERIFY against the specific warranty terms in force.

| Item | RIT field(s) | Notes |
|---|---|---|
| Unit identification: model, serial, purchase/commissioning date | `robot_make/model/serial` | Commissioning date from integrator records |
| Description of defect and circumstances | `narrative`, FM codes | FM-06 (mechanical) and FM-07 (battery) are the classic warranty modes |
| Proof the unit was maintained per schedule | EV-05 | Missing maintenance records are the standard warranty-denial ground |
| Software/firmware version at failure | EV-06 | Establishes whether an OTA update (FM-08) is implicated — which may shift the claim from warranty to the software vendor (PT-03) |
| Operating conditions within spec | EV-07 | OEMs deny for out-of-spec environments (wet floors, temperature, ramps) |
| Logs demonstrating the failure | EV-02 | Raw exports; keep your own copy independent of the OEM's telemetry |
| Photos/video of the failure and damage | EV-01, EV-03 | |
| No third-party tampering | EV-03, EV-04, FM-05 absent/present | Interference (FM-05) usually voids the warranty path but opens PT-06 recovery |

## 3. RaaS / SLA claim pack (against the integrator or RaaS operator — PT-04)

For service credits, remedy obligations, or contractual damages under a robotics-as-a-service or integration contract. TO VERIFY against the actual SLA.

| Item | RIT field(s) | Notes |
|---|---|---|
| Incident timestamp and detection time | `incident_at`, `created_at` | SLAs often run remedy clocks from notification — notify in the contractual channel, in writing, fast |
| Downtime quantification | `downtime_hours`, HT-05 | Distinguish robot-down from site-function-impaired; SLAs usually credit only the former unless negotiated |
| Task being performed | TK code | Establishes the failure occurred in contracted service scope |
| Fleet context | `fleet_size_at_site` | Whether sibling units covered the gap affects business-interruption quantum |
| Operator/teleop involvement | TK-11, FM-09, PT-05 | If a teleoperator was in control, the teleop provider's obligations activate |
| Root-cause allocation evidence | FM codes + EV-02, EV-06 | The SLA fight is almost always "your misuse (FM-04) vs. our system (FM-01/02/03/08)" — logs decide it |
| Prior incident/defect history for this unit | Prior RIT records, EV-05 | Pattern evidence converts a one-off credit into a remedy/replacement claim |

## 4. Insurance claim pack (deployer's carrier, or third party's carrier — PT-01/PT-06)

Covers general liability (injury, third-party property), commercial property (own damage, stock), and business interruption. TO VERIFY against policy terms; robot-specific policies/endorsements are new and vary widely.

| Item | RIT field(s) | Notes |
|---|---|---|
| First notice of loss: date, time, location, what happened | `incident_at`, `narrative`, EN code | Late notice is a coverage risk — notify even while investigation is open (`record_status: open`) |
| Injured party details and treatment | HT-01, `injured_party_role`, EV-04 | First-aid log, medical attention received, whether they declined care |
| Damage inventory and valuation | HT-02/03/04, `estimated_total_cost`, EV-01 | Separate own property, third-party property, and stock — they may fall under different coverages |
| Business-interruption computation | HT-05, `downtime_hours` | Revenue impact evidence (sales data for the affected period vs. baseline) |
| Scene and cause evidence | EV-01, EV-03, EV-07, EV-08, FM codes | Carriers subrogate: clean FM coding pointing at the OEM/vendor helps your carrier recover, which helps your renewal |
| Robot maintenance and software history | EV-05, EV-06 | Demonstrates deployer diligence; rebuts contributory-negligence arguments |
| Witness statements | EV-04 | Signed where possible |
| Contracts in the chain | — (attach) | OEM warranty, RaaS/SLA, teleop agreement — indemnity and additional-insured clauses determine who ultimately pays |
| Regulatory reports filed, if any | — (attach) | OSHA/local equivalents where applicable (TO VERIFY jurisdiction-specific duties) |
| Severity coding | SV | Not required by carriers today, but a consistent SV history across your fleet is exactly the loss-run evidence that earns better pricing at renewal |

## 5. Cross-claim consistency check

One incident, three audiences — inconsistencies between packs are how claims die.

- [ ] Same timeline in all three packs (use the RIT record as the single source of truth).
- [ ] Same cost figures (`estimated_total_cost` reconciles with every itemization submitted).
- [ ] FM coding consistent with each narrative — do not tell the OEM "hardware failure" and the carrier "software regression".
- [ ] Every evidence item referenced in any pack exists in the RIT `evidence` array with its location/custodian noted.
- [ ] `record_status` moved to `closed` only after all claim paths resolve; final costs written back to the record.

---

*Why this matters beyond the claim: every completed checklist is a fully-coded, evidence-backed RIT record. Consistent records across many deployers are the loss-history corpus that robot insurance currently lacks — the thing Lossbook exists to build.*
