# Lossbook

**The loss-data bureau for physical AI.**

Robots are moving out of Amazon-scale facilities and into ordinary businesses — cleaning robots in supermarkets, AMRs in 20-person warehouses, delivery and security robots, early humanoid pilots — and insurers are pricing the risk nearly blind: there is no shared loss history for robot incidents, no standard way to describe one, and every claim is a documentation fight between the deployer, the OEM, the software vendor, and the integrator. Lossbook's thesis is that robot liability will become a standard commercial insurance line over the next five years, standard lines run on shared loss data, and the neutral bureau that pools that data — the Verisk of the robot economy — does not exist yet. The first brick is a common language for what went wrong.

## Why the taxonomy is free

The taxonomy in this repo is published as an open standard (CC BY 4.0), deliberately. This is the ACORD-forms strategy: ACORD gave the insurance industry its standard forms for free and became the default everyone builds on; ISO/Verisk turned pooled, consistently-coded loss data into infrastructure. The open taxonomy is the standard; the data bureau built on top of it comes later. Anyone — deployers, RaaS operators, OEMs, brokers, carriers, researchers — is encouraged to adopt it, extend it, and code incidents with it. Every incident recorded in this format anywhere increases the option value of the pooled corpus that no single OEM or carrier can assemble alone.

## Status

**v0.1 published draft (2026-07-19)** — open for review and adoption. Feedback and field experience welcome via issues; see `BACKLOG.md` for the v0.2 review agenda.

## Repo layout

| Path | What it is |
|---|---|
| `taxonomy/robot-incident-taxonomy-v0.1.md` | The core deliverable: the standardized robot-incident taxonomy — coded fields, enumerated values, severity scale, worked example, JSON schema |
| `taxonomy/evidence-pack-checklist.md` | The one-click evidence pack as a checklist: what a warranty / RaaS-SLA / insurance claim needs documented, mapped to taxonomy fields |
| `schemas/rit-record-0.1.json` | Canonical machine-readable JSON Schema for an incident record (same schema as §12 of the taxonomy) |
| `LICENSE.md` | CC BY 4.0 for the taxonomy documents |
| `PUBLISH.md` | Publication plan and options, awaiting owner approval |
| `BACKLOG.md` | v0.2 review tasks and guardrails (notably: do not build the SaaS yet) |

## What this repo is not

No software, no SaaS, no data collection. Per the portfolio plan, the only asset being built now is the standard itself — days of work, permanent option value.
