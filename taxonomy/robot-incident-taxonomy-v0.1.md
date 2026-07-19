# Robot Incident Taxonomy (RIT) — v0.1 DRAFT

**A standardized taxonomy for incidents and near-misses involving robots in commercial deployments.**

| | |
|---|---|
| Version | 0.1 (draft for review — not yet published) |
| Status | DRAFT — field codes and enumerations are stable within v0.x unless marked otherwise; new codes may be appended |
| License | CC BY 4.0 (see `../LICENSE.md`) |
| Maintainer | Lossbook |
| Record format | One record per incident, fields below; machine format defined by the JSON Schema in §12 |

---

## 1. Purpose and scope

This taxonomy defines a common, coded language for describing **incidents and near-misses involving robots deployed in commercial settings**. It is designed so that:

1. A deployer, RaaS operator, or integrator can capture an incident consistently at the time it happens, with fields that map directly onto what warranty, SLA, and insurance claims later require (see `evidence-pack-checklist.md`).
2. Records from different fleets, vendors, and industries can be aggregated into comparable frequency/severity statistics by robot class, task, environment, and failure mode.
3. No field forces disclosure of proprietary technology. The taxonomy describes *what happened and what it cost*, not how the robot works.

**In scope:** any unplanned event involving a robot in a commercial deployment that caused, or plausibly could have caused, harm — including near-misses with no harm.

**Out of scope (v0.1):** military systems, surgical robots, autonomous passenger vehicles on public roads (these have their own regulatory reporting regimes), hobby/consumer home robots. Sidewalk delivery robots **are** in scope. TO VERIFY: whether aerial drones should be a robot class in v0.2 or remain out of scope.

## 2. Conventions

- Every enumerated value has a stable code (`XX-nn`). Codes are never reused or renumbered; deprecated codes are marked deprecated and retained.
- `-99` is always "other (describe in free text)"; `-98` (where present) is always "unknown / not yet determined".
- Fields marked **(multi)** accept multiple codes.
- All free-text fields are supplementary; the coded fields alone must be sufficient for statistical aggregation.
- Timestamps are ISO 8601 with timezone offset. Currency amounts are ISO 4217 code + decimal value.
- A **near-miss** is an incident with harm type `HT-00` only. Near-misses use the same record format — leading-indicator data is the point.

## 3. Field RC — Robot class

The class of the robot primarily involved. Classify by function as deployed, not by marketing name. If two robots are involved, file one record with the primary robot's class and note the second in the narrative (v0.2 may add multi-robot support).

| Code | Value | Notes / boundary rules |
|---|---|---|
| RC-01 | AMR (autonomous mobile robot) | Free-navigating mobile base (SLAM or similar); includes tote/shelf carriers, AMR forklifts |
| RC-02 | AGV (automated guided vehicle) | Fixed guidance: wire, magnetic tape, QR grid, rail. If it path-plans freely, use RC-01 |
| RC-03 | Fixed-arm industrial | Caged or safety-zoned manipulator, not designed for human proximity |
| RC-04 | Cobot (collaborative arm) | Manipulator rated for collaborative operation alongside humans |
| RC-05 | Cleaning robot | Floor scrubbers, vacuums, disinfection units, window cleaners |
| RC-06 | Delivery robot — sidewalk / outdoor | Operates on public or semi-public outdoor ways |
| RC-07 | Delivery robot — indoor | In-building couriers: hotels, hospitals, offices, restaurants |
| RC-08 | Security / inspection robot | Patrol, surveillance, remote-inspection units (ground-based) |
| RC-09 | Agricultural robot | Field, orchard, greenhouse, or barn robots; includes autonomous tractors operating off public roads |
| RC-10 | Humanoid / general-purpose bipedal | Bipedal or wheeled-humanoid general-purpose platforms |
| RC-99 | Other | Describe in `robot_class_other` |

## 4. Field EN — Deployment environment

Where the robot was operating when the incident occurred.

| Code | Value | Notes |
|---|---|---|
| EN-01 | Warehouse / distribution / fulfillment | Includes cold storage |
| EN-02 | Retail floor | Customer-facing store areas; back-of-store stockrooms count as EN-01 |
| EN-03 | Hospital / healthcare facility | Includes clinics, labs, elder-care facilities |
| EN-04 | Restaurant / commercial kitchen | Front- or back-of-house food service |
| EN-05 | Outdoor public way | Sidewalks, crosswalks, plazas, campuses open to the public |
| EN-06 | Construction site | |
| EN-07 | Agricultural land / facility | Fields, orchards, greenhouses, barns |
| EN-08 | Office / commercial building interior | Offices, lobbies, hotels (non-restaurant areas) |
| EN-09 | Manufacturing / production floor | Factory environments distinct from warehousing |
| EN-99 | Other | Describe in `environment_other` |

*Note: EN-09 added beyond the v0.1 outline because fixed-arm and cobot incidents (RC-03/RC-04) predominantly occur there and would otherwise pollute EN-99.*

## 5. Field TK — Task at time of incident

What the robot was doing (or commanded to do) when the incident began.

| Code | Value |
|---|---|
| TK-01 | Transit / navigation between points (no payload interaction in progress) |
| TK-02 | Picking, placing, or manipulating items |
| TK-03 | Transporting a payload / towing |
| TK-04 | Cleaning / surface treatment in progress |
| TK-05 | Delivery handoff (loading or unloading with a human or dock) |
| TK-06 | Patrol / inspection / data capture |
| TK-07 | Docking, charging, or battery swap |
| TK-08 | Mapping, calibration, or commissioning run |
| TK-09 | Idle / parked / awaiting task |
| TK-10 | Under maintenance, service, or manual repositioning |
| TK-11 | Teleoperated maneuver (human remotely in control at the time) |
| TK-99 | Other |

## 6. Field FM — Incident trigger / failure mode **(multi)**

The proximate trigger(s) that initiated the incident. Record the *initiating* failure; contributing factors go in `contributing_factors` using the same codes. If root cause is not yet established, use FM-98 and update the record when the investigation closes (`record_status` tracks this).

| Code | Value | Includes |
|---|---|---|
| FM-01 | Perception failure | Missed/false obstacle detection, misclassification, sensor occlusion or degradation |
| FM-02 | Localization / mapping failure | Lost localization, stale or corrupted map, drift, wrong-floor errors |
| FM-03 | Planning / decision failure | Legal-but-wrong path or action choice, deadlock, unsafe speed for context, faulty task logic |
| FM-04 | Human error (on-site) | Operator misuse, bypassed safeguards, incorrect load, blocked sensors, wrong configuration by site staff |
| FM-05 | Third-party interference | Vandalism, tampering, theft, deliberate obstruction, assault on robot |
| FM-06 | Mechanical / hardware failure | Structural, drivetrain, brake, gripper, sensor hardware failure, wheel/track loss |
| FM-07 | Battery / charging system | Thermal event, charge failure, unexpected power loss, dock fault |
| FM-08 | Software update / regression | Behavior change following an update, failed OTA, version mismatch |
| FM-09 | Network / teleoperation loss | Connectivity loss, latency, teleop session drop, cloud dependency outage |
| FM-10 | Environmental | Spills, weather, lighting, floor condition, temperature, unexpected static obstacles |
| FM-11 | Security incident (cyber) | Unauthorized access, spoofed commands, jamming. *Added in v0.1 draft; distinct from FM-05 physical interference* |
| FM-98 | Unknown / under investigation | |
| FM-99 | Other | |

## 7. Field HT — Harm type **(multi)**

All harm categories that materialized. A record with only `HT-00` is a near-miss.

| Code | Value | Notes |
|---|---|---|
| HT-00 | None / near-miss | No harm materialized; incident had plausible potential for harm |
| HT-01 | Personal injury | Any injury to any person; role of injured party captured in `injured_party_role` |
| HT-02 | Property damage — own / deployer's | Damage to deployer's premises, equipment, or the robot itself |
| HT-03 | Property damage — third party | Damage to property of customers, visitors, neighbors, other businesses |
| HT-04 | Product / stock loss | Damaged, destroyed, or contaminated inventory or work-in-progress |
| HT-05 | Downtime / business interruption | Lost operating time of the robot, the fleet, or the site |
| HT-06 | Data / privacy harm | Unauthorized capture, exposure, or loss of personal or business data |
| HT-07 | Environmental harm | Spill, emission, fire spread, contamination beyond the site |

## 8. Field SV — Severity scale (0–5)

One value per record: the **highest** band reached on *any* dimension (injury, cost, downtime, response). Monetary anchors are total incident cost (all HT categories combined, best estimate at time of last update) in USD; adopters in other currencies should convert at incident-date rates. TO VERIFY: anchor amounts should be sanity-checked against carrier deductible/attachment conventions before v1.0.

| Code | Level | Injury anchor | Cost anchor (total, USD) | Downtime anchor | Response anchor |
|---|---|---|---|---|---|
| SV-0 | Near-miss | None | < $100 | Momentary stop only (< 15 min) | Self-recovered or single on-site reset |
| SV-1 | Negligible | None | $100 – $1,000 | Robot out < 1 h; no site impact | On-site staff resolved |
| SV-2 | Minor | First-aid only, no medical treatment | $1,000 – $10,000 | Robot out 1–24 h, or brief partial site slowdown | Vendor remote support engaged |
| SV-3 | Serious | Medical treatment beyond first aid, no hospitalization | $10,000 – $100,000 | Robot out 1–7 days, or site function materially impaired ≤ 1 day | Vendor on-site; incident review required; regulator notification may apply |
| SV-4 | Severe | Hospitalization or lost-time injury | $100,000 – $1,000,000 | Robot/fleet out > 7 days, or site materially impaired > 1 day | Fleet grounding; formal investigation; insurer notified |
| SV-5 | Critical | Fatality or permanent impairment | > $1,000,000 | Site shutdown of indefinite duration | Regulator involvement mandatory; litigation expected |

Rule: an incident with a hospitalized person and $500 of damage is SV-4. When in doubt between two bands, code the higher and note the doubt in the narrative.

## 9. Field PT — Parties potentially implicated **(multi)**

Parties whose acts, omissions, products, or services are *potentially* implicated in cause or liability. This is a documentation aid, not a legal determination — code inclusively at capture time.

| Code | Value | Typical exposure |
|---|---|---|
| PT-01 | Deployer (site operator) | Premises liability, supervision, misuse, maintenance lapses |
| PT-02 | Robot OEM / manufacturer | Product defect, design, warnings, hardware warranty |
| PT-03 | Software vendor (if distinct from OEM) | Autonomy stack, fleet manager, update regressions |
| PT-04 | Integrator / RaaS operator | Installation, configuration, fleet operation, SLA obligations |
| PT-05 | Teleoperation provider | Remote-operator error, session handling, staffing |
| PT-06 | Third party | Interfering individuals, other contractors, adjacent businesses, members of the public |
| PT-99 | Other | e.g. facility landlord, utility, network carrier |

## 10. Field EV — Evidence captured **(multi)**

What evidence exists for this incident, coded so a claims handler can see completeness at a glance. Detail per item goes in the `evidence` array of the record (§11). The companion document `evidence-pack-checklist.md` maps these to warranty/SLA/insurance claim requirements.

| Code | Value | Capture guidance |
|---|---|---|
| EV-01 | Photographs | Scene, damage, robot position, sensor obstructions; timestamped |
| EV-02 | Robot logs | On-board and fleet-manager logs covering ≥ 30 min before the incident; preserve raw exports |
| EV-03 | Video | Robot cameras and/or site CCTV; note retention deadline — CCTV often auto-deletes in 7–30 days |
| EV-04 | Witness statements | Name, role, contact, signed statement or contemporaneous note |
| EV-05 | Maintenance history | Service records, open defect list, last inspection date for the unit involved |
| EV-06 | Software version record | Autonomy stack, firmware, map version; date of last update — critical if FM-08 suspected |
| EV-07 | Environmental conditions | Floor state, weather, lighting, temperature, obstructions; photos count double |
| EV-08 | Incident scene preservation | Whether the scene/robot state was preserved before reset; time of first reset |

## 11. Record format

A RIT record consists of administrative metadata plus the coded fields above. Normative machine format is the JSON Schema in §12; the tables below are the human definition.

**Administrative:** `record_id` (UUID), `record_status` (`open` | `updated` | `closed`), `schema_version` ("0.1"), `created_at`, `updated_at`, `reporter_role` (free text), `incident_at` (timestamp), `incident_tz_local_time`.

**Robot identity:** `robot_make`, `robot_model`, `robot_serial` — free text; serial may be pseudonymized for sharing. `fleet_size_at_site` (integer) enables frequency-per-robot statistics.

**Coded fields:** `robot_class` (RC), `environment` (EN), `task` (TK), `failure_modes` (FM, multi), `contributing_factors` (FM codes, multi, optional), `harm_types` (HT, multi), `severity` (SV), `parties_implicated` (PT, multi), `evidence_captured` (EV, multi).

**Impact detail:** `injured_party_role` (`employee` | `customer` | `visitor` | `public` | `contractor` | `none`), `estimated_total_cost` ({currency, amount}), `downtime_hours` (number), `narrative` (free text).

### Worked example

> A floor-scrubbing robot in a supermarket, mid-clean on a Saturday morning, fails to detect a clear liquid spill (its own leaked cleaning fluid, per later investigation), drives through it, and loses traction; it bumps a promotional display, which topples. A customer stepping away from the display twists an ankle — treated on-site by first aid, declines further care. Store loses the aisle for 2 hours; display stock written off at ~$800; robot undamaged. CCTV captured the event; robot logs pulled the same day.

```json
{
  "record_id": "3f7c2a90-5b1e-4d68-9a44-1c2ab9e0f512",
  "schema_version": "0.1",
  "record_status": "closed",
  "created_at": "2026-07-11T10:42:00-05:00",
  "updated_at": "2026-07-15T09:00:00-05:00",
  "reporter_role": "store operations manager",
  "incident_at": "2026-07-11T09:58:00-05:00",
  "robot_make": "ExampleCo",
  "robot_model": "Scrub-X 400",
  "robot_serial": "PSEUDO-8842",
  "fleet_size_at_site": 2,
  "robot_class": "RC-05",
  "environment": "EN-02",
  "task": "TK-04",
  "failure_modes": ["FM-01", "FM-06"],
  "contributing_factors": ["FM-10"],
  "harm_types": ["HT-01", "HT-02", "HT-04", "HT-05"],
  "severity": "SV-2",
  "injured_party_role": "customer",
  "parties_implicated": ["PT-01", "PT-02", "PT-04"],
  "evidence_captured": ["EV-01", "EV-02", "EV-03", "EV-04", "EV-05", "EV-06", "EV-07"],
  "estimated_total_cost": { "currency": "USD", "amount": 2350.00 },
  "downtime_hours": 2.0,
  "evidence": [
    { "code": "EV-03", "description": "Store CCTV cam 14, 09:55-10:05, exported 2026-07-11" },
    { "code": "EV-02", "description": "Robot + fleet-manager logs 09:30-10:15, raw export retained" },
    { "code": "EV-06", "description": "Firmware 4.2.1, autonomy stack 2026.06 release, last OTA 2026-07-02" }
  ],
  "narrative": "Scrubber leaked cleaning fluid (suspected pump seal failure, FM-06), then failed to detect the resulting clear spill (FM-01), lost traction and contacted a promotional display. Customer near display sustained minor ankle injury, first aid only, declined treatment. Aisle closed ~2h. OEM notified re: pump seal; RaaS operator performed fleet check on sibling unit."
}
```

Coding notes on the example: the *initiating* failure is coded as both FM-01 (the spill went undetected) and FM-06 (the leak originated in hardware); the wet floor itself is a contributing environmental factor (FM-10). Severity is SV-2 (first-aid-only injury is the highest band reached). PT-02 and PT-04 are coded inclusively — the pump seal implicates the OEM, fleet maintenance implicates the RaaS operator — without asserting liability.

## 12. JSON Schema (v0.1)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://lossbook.example/schemas/rit-record-0.1.json",
  "title": "RIT Incident Record v0.1",
  "type": "object",
  "required": [
    "record_id", "schema_version", "record_status", "created_at",
    "incident_at", "robot_class", "environment", "task",
    "failure_modes", "harm_types", "severity", "parties_implicated",
    "evidence_captured", "narrative"
  ],
  "properties": {
    "record_id": { "type": "string", "format": "uuid" },
    "schema_version": { "const": "0.1" },
    "record_status": { "enum": ["open", "updated", "closed"] },
    "created_at": { "type": "string", "format": "date-time" },
    "updated_at": { "type": "string", "format": "date-time" },
    "reporter_role": { "type": "string" },
    "incident_at": { "type": "string", "format": "date-time" },
    "robot_make": { "type": "string" },
    "robot_model": { "type": "string" },
    "robot_serial": { "type": "string" },
    "fleet_size_at_site": { "type": "integer", "minimum": 1 },
    "robot_class": { "enum": ["RC-01","RC-02","RC-03","RC-04","RC-05","RC-06","RC-07","RC-08","RC-09","RC-10","RC-99"] },
    "robot_class_other": { "type": "string" },
    "environment": { "enum": ["EN-01","EN-02","EN-03","EN-04","EN-05","EN-06","EN-07","EN-08","EN-09","EN-99"] },
    "environment_other": { "type": "string" },
    "task": { "enum": ["TK-01","TK-02","TK-03","TK-04","TK-05","TK-06","TK-07","TK-08","TK-09","TK-10","TK-11","TK-99"] },
    "failure_modes": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "enum": ["FM-01","FM-02","FM-03","FM-04","FM-05","FM-06","FM-07","FM-08","FM-09","FM-10","FM-11","FM-98","FM-99"] }
    },
    "contributing_factors": {
      "type": "array", "uniqueItems": true,
      "items": { "enum": ["FM-01","FM-02","FM-03","FM-04","FM-05","FM-06","FM-07","FM-08","FM-09","FM-10","FM-11","FM-98","FM-99"] }
    },
    "harm_types": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "enum": ["HT-00","HT-01","HT-02","HT-03","HT-04","HT-05","HT-06","HT-07"] }
    },
    "severity": { "enum": ["SV-0","SV-1","SV-2","SV-3","SV-4","SV-5"] },
    "injured_party_role": { "enum": ["employee","customer","visitor","public","contractor","none"] },
    "parties_implicated": {
      "type": "array", "minItems": 1, "uniqueItems": true,
      "items": { "enum": ["PT-01","PT-02","PT-03","PT-04","PT-05","PT-06","PT-99"] }
    },
    "evidence_captured": {
      "type": "array", "uniqueItems": true,
      "items": { "enum": ["EV-01","EV-02","EV-03","EV-04","EV-05","EV-06","EV-07","EV-08"] }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["code", "description"],
        "properties": {
          "code": { "enum": ["EV-01","EV-02","EV-03","EV-04","EV-05","EV-06","EV-07","EV-08"] },
          "description": { "type": "string" }
        }
      }
    },
    "estimated_total_cost": {
      "type": "object",
      "required": ["currency", "amount"],
      "properties": {
        "currency": { "type": "string", "pattern": "^[A-Z]{3}$" },
        "amount": { "type": "number", "minimum": 0 }
      }
    },
    "downtime_hours": { "type": "number", "minimum": 0 },
    "narrative": { "type": "string", "minLength": 1 }
  },
  "allOf": [
    {
      "if": { "properties": { "harm_types": { "contains": { "const": "HT-01" } } }, "required": ["harm_types"] },
      "then": { "required": ["injured_party_role"] }
    }
  ]
}
```

## 13. Versioning and change policy

- v0.x drafts: codes may be **appended**, never renumbered or reused. Semantic changes to an existing code require a new code plus deprecation of the old one.
- v1.0 will be declared after external review (see `../BACKLOG.md`) and will freeze required fields.
- Records always carry `schema_version`; aggregators must treat unknown codes as `-99` of the relevant field rather than rejecting the record.

## 14. Known gaps (candidates for v0.2)

- Aerial drones: in or out of scope (TO VERIFY with prospective users).
- Multi-robot incidents (robot–robot collisions) — currently a single-record convention.
- Regulatory-reporting cross-references (OSHA recordability, EU Machinery Regulation incident duties) — TO VERIFY exact mappings before claiming them.
- Injury severity sub-coding (e.g. abbreviated injury scale alignment) if carriers request it.
- Anonymization/pseudonymization profile for sharing records into a pooled corpus.
