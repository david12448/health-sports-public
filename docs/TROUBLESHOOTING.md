# Troubleshooting

Record date, issue, root cause, fix, test evidence, and regression precautions here.

## Initial setup
- No known implementation failures yet.

## 2026-10-10 — Source licensing and safety caveats
- Issue: KDCA Korean 2025 CPR guideline is KOGL type 4; commercial republication or adaptation of original diagrams/text is not permitted under that license.
- Prevention: private reference-only pointer; no copying to public catalog; arrange separate rights clearance or create independently written medically checked information.
- Issue: HIRA hospital finder limits bulk Excel download to 100 due to excessive scraping; official public data files/APIs exist.
- Prevention: obtain data from authorized data.go.kr services after checking terms; do not bulk scrape the map UI.
- Test result: validator checks passed; it does not verify medical accuracy, license clearance, or live page deployment.
