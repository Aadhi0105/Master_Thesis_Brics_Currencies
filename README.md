# BRICS Currencies and Global Monetary Fragmentation
### Master's Thesis — Empirical Analysis of Local Currency Settlement in International Trade (2010–2025)

**Author:** Aadhitya Tejaswin Prakash Sridevi  
**Programme:** Master in Management (Business Management), EDHEC Business School  
**Exchange:** University of St. Gallen (HSG) — Full-Year Exchange, Quantitative Economics  
**Supervisor:** [Mirco Rubin], EDHEC Business School  
**Status:** Data collection complete — entering empirical analysis phase (March 2026)

---

## Overview

This thesis investigates the role of BRICS currencies — the Chinese Renminbi (CNY), Russian Rouble (RUB), Indian Rupee (INR), Brazilian Real (BRL), and South African Rand (ZAR) — in international trade settlement between 2010 and 2025. The central question is whether these currencies have achieved meaningful internationalisation as media of exchange in global trade, or whether the international monetary system remains structurally anchored to the US Dollar despite geopolitical shifts that might have been expected to accelerate de-dollarisation.

The thesis is theoretically grounded in Gopinath's **Dominant Currency Paradigm (DCP)**, which holds that a small number of dominant currencies — principally the USD — invoice and settle the majority of global trade irrespective of the bilateral trading partners involved. This thesis tests whether the post-2022 sanctions shock to Russia and the systematic expansion of China's cross-border payment infrastructure (CIPS) have begun to structurally challenge this paradigm at the BRICS level.

The work engages directly with sceptical literature on BRICS currency internationalisation, which argues that capital account restrictions, shallow financial markets, and lack of institutional trust continue to constrain the international use of non-dollar BRICS currencies.

---

## Research Questions

1. Has the concentration of global payment currencies (as measured by the Herfindahl-Hirschman Index) declined between 2010 and 2025, and if so, which BRICS currencies have contributed to this shift?
2. What bilateral and macroeconomic factors determine the share of local currency settlement in BRICS trade relationships?
3. Have discrete policy events — in particular the exclusion of Russia from SWIFT in February 2022 and the launch of China's CIPS infrastructure — caused measurable, causal shifts in local currency settlement patterns?

---

## Empirical Strategy

The thesis employs three complementary empirical methods:

### Equation 1 — HHI Concentration Analysis
A Herfindahl-Hirschman Index computed annually from SWIFT global payment currency shares (2013–2025) and IMF COFER reserve composition data (2010–2025). This tracks the evolution of currency concentration in both the payments and reserve dimensions, and disaggregates the contribution of individual BRICS currencies over time.

### Equation 2 — Fixed-Effects Panel Regression
A bilateral panel regression estimating the determinants of local currency settlement share (LCShare) across BRICS country pairs and their major trading partners (2010–2024). The dependent variable is a proxy constructed from SWIFT aggregate payment data and BIS Locational Banking Statistics. Independent variables include bilateral trade intensity (IMF DOTS), FX volatility (IMF Exchange Rates), GDP, trade openness, inflation, and broad money growth (World Bank WDI).

### Equation 3 — Difference-in-Differences (DiD)
An event-study design estimating the causal effect of eight discrete policy events on local currency settlement. The strongest identification comes from the Russia SWIFT exclusion (February 2022), which provides a large, discrete, and well-documented treatment. Additional events include the CIPS Phase 1 and Phase 2 launches, the India-Russia Rupee Framework, the Brazil-China RMB Agreement, and the BRICS Johannesburg Summit Declaration (2023). The parallel trends assumption and spillover effects will be reviewed with the thesis supervisor and an external methodology consultant at HSG.

---

## Repository Structure

```
Master_Thesis_Brics_Currencies/
│
├── notebooks/                        # Jupyter notebooks for data cleaning and analysis
│   └── [to be populated]
│
├── scripts/                          # Python scripts for data extraction and processing
│   └── extract_swift_v2.py           # SWIFT RMB Tracker data extraction (v2)
│
├── outputs/                          # Processed datasets and figures
│   └── [to be populated]
│
├── DATA_MANIFEST.md                  # Full dataset inventory with citations and gap notes
└── README.md                         # This file
```

> **Note:** Raw data files are stored locally at `/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/` and are not tracked in this repository. Word documents are excluded via `.gitignore`. The canonical record of data collection status is `DATA_MANIFEST.md`.

---

## Data Sources

All eight primary datasets have been collected as of 22 March 2026. Full citations and file-level details are in `DATA_MANIFEST.md`.

| Dataset | Coverage | Role in Analysis |
|---------|----------|-----------------|
| SWIFT Global Currency Tracker | 2013–2025 (annual HHI); 2019–2026 (monthly CNY share) | Equation 1 (HHI); LCShare proxy component |
| BIS Locational Banking Statistics | 1977–2025 Q3 | LCShare proxy component; financial linkage variable |
| IMF COFER | 2010–2025 Q3 | Equation 1 (reserve concentration) |
| IMF DOTS / IMTS | 2010–2024 | Equation 2 (trade intensity regressor) |
| IMF Exchange Rates | 2010–2026 | Equation 2 (FX volatility control) |
| World Bank WDI | 2010–2024 | Equation 2 (macro controls) |
| Policy Events Dataset | 2015–2023 | Equation 3 (DiD treatment assignment) |
| UN Comtrade | 2010–2024 | Cross-validation of DOTS bilateral trade figures |

### Key Data Notes
- **LCShare dependent variable:** No direct bilateral currency settlement data exists in public sources. LCShare is constructed as a proxy from SWIFT aggregate payment shares and BIS LBS dollar-share data. This limitation is acknowledged and addressed in the methodology chapter.
- **SWIFT HHI 2021:** Unavailable from public archives. Treated as a missing observation rather than interpolated, given the structural volatility of the COVID-19 recovery period and proximity to the 2022 Russia sanctions shock.
- **SWIFT HHI 2013:** Available from Wayback Machine archive but sourced from a low-resolution image; treated as approximate pending verification.
- **UN Comtrade:** Used solely as a cross-validation instrument for DOTS trade figures (right-hand side of Equation 2 only). Comtrade records trade values in USD, not currency of settlement, and cannot serve as an LCShare source.
- **SWIFT undercounting:** SWIFT data systematically undercounts local currency settlement because CIPS (China) and SPFS (Russia) route payments outside the SWIFT network. This is flagged explicitly in the methodology and addressed through BIS CPMI supplementary data.

---

## Progress to Date

### Completed
- [x] Thesis proposal submitted and approved by EDHEC supervisor
- [x] Theoretical framework established (Dominant Currency Paradigm; sceptical literature review)
- [x] Three-equation empirical strategy designed (HHI, panel regression, DiD)
- [x] Full data collection across all eight sources (completed 22 March 2026)
- [x] SWIFT HHI annual series supplemented back to 2013 via Wayback Machine archive
- [x] Policy Events Dataset constructed (8 events, 2015–2023)
- [x] FX volatility computed from IMF monthly exchange rate series
- [x] UN Comtrade cross-validated against IMF DOTS — deviations below 1% for all major BRICS pairs
- [x] Data gap assessment documented (see `DATA_MANIFEST.md`)
- [x] Git repository initialised with structured folder layout

### In Progress / Upcoming
- [ ] Supervisor update (Monday 23 March 2026)
- [ ] Meeting with HSG macroeconomics professor — DiD identification strategy and LCShare proxy methodology
- [ ] Python data cleaning notebooks — merging, standardisation, panel construction
- [ ] LCShare proxy variable construction from SWIFT + BIS LBS
- [ ] HHI computation and visualisation (Equation 1)
- [ ] Fixed-effects panel regression (Equation 2)
- [ ] Difference-in-Differences estimation (Equation 3)
- [ ] Literature review chapter (incorporating sceptical literature)
- [ ] Methodology chapter
- [ ] Results and discussion chapters
- [ ] Thesis submission
- [ ] Pre-doctoral application to University of Zurich (UZH)
- [ ] Journal submission (target: post-thesis)

---

## Known Methodological Challenges

| Challenge | Status |
|-----------|--------|
| LCShare proxy relies on indirect sources (SWIFT + BIS LBS) rather than direct settlement data | Acknowledged; discussed in methodology |
| SWIFT systematically undercounts via CIPS/SPFS | Flagged; BIS CPMI supplement planned |
| DiD parallel trends assumption — CIPS gradual rollout complicates clean identification | To be reviewed with HSG professor |
| Russia sanctions create global spillover effects, complicating clean DiD control group | To be reviewed with HSG professor |
| HHI measure is aggregate — may mask bilateral heterogeneity | Addressed via supervisor-recommended extension to individual BRICS currencies |
| CNY COFER data only available from 2016-Q4 | Known institutional fact; stated in methodology |

---

## Contact

**Aadhitya Tejaswin Prakash Sridevi**  
Master in Management (Business Management), EDHEC Business School  
Full-Year Exchange in Quantitative Economics, University of St. Gallen (HSG)  
GitHub: [Aadhi0105](https://github.com/Aadhi0105)

---

*Last updated: 22 March 2026*