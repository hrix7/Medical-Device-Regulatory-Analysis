# Medical Device Regulatory Analysis

I created this repository from my graduate regulatory work on end-stage renal disease (ESRD) and wearable artificial kidney technology. My analysis connected the clinical need, device risks, evidence expectations, and possible U.S. regulatory pathways.

## Work I completed

- Reviewed limitations of conventional dialysis and the clinical motivation for wearable renal-replacement systems.
- Compared FDA 510(k), De Novo, and premarket approval concepts.
- Examined how intended use, technological characteristics, and risk influence pathway selection.
- Structured hazard, hazardous-situation, harm, probability, severity, and risk-control information.
- Considered software, alarms, fluid handling, electrical safety, biocompatibility, and human factors.
- Prepared a 15-25 page IEEE-style technical/regulatory report.
- Expanded my regulatory experience to SaMD, EU IVDR, and FMEA concepts.

## Repository code

- `src/risk_matrix.py` validates and scores a 1-5 severity/probability risk table.
- `src/pathway_decision.py` produces a transparent educational comparison of common U.S. pathway considerations.
- `examples/sample_risks.csv` shows the risk-table structure using non-product-specific examples.
- `docs/REGULATORY_RESEARCH_TEMPLATE.md` is the outline I use to organize regulatory research.

## Run the tools

```bash
python -m pip install -r requirements.txt
python src/risk_matrix.py examples/sample_risks.csv
python src/pathway_decision.py --predicate no --risk high --novel yes
```

## Topics

FDA 510(k), De Novo, PMA, SaMD, EU IVDR, FMEA, risk management, clinical evidence, human factors, wearable artificial kidney.

## Scope

This repository documents academic work and reusable research tools. It is not regulatory, legal, or submission advice for a specific commercial device.

## Author and Project Setting

**Hritika Adhikary**  
BMD 667 - Regulation of Medical Diagnostics and Devices  
Arizona State University  
Spring 2025

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
