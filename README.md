# BRICS Currencies and Global Monetary Fragmentation
### Master's Thesis — Empirical Analysis of Local Currency Settlement in International Trade (2010–2025)

**Author:** Aadhitya Tejaswin Prakash Sridevi  
**Programme:** Master in Management (Business Management), EDHEC Business School  
**Exchange:** University of St. Gallen (HSG) — Full-Year Exchange, Quantitative Economics  
**Supervisor:** EDHEC Business School  
**Status:** Data collection and panel construction complete — entering empirical analysis phase (May 2026)

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
An event-study design estimating the causal effect of eight discrete policy events on local currency settlement. The strongest identification comes from the Russia SWIFT exclusion (February 2022), which provides a large, discrete, and well-documented treatment. Additional events include the CIPS Phase 1 and Phase 2 launches, the India-Russia Rupee Framework, the Brazil-China RMB Agreement, and the BRICS Johannesburg Summit Declaration (2023). The parallel trends assumption and spillover effects are under review with the HSG methodology advisor.

---

## Repository Structure

```
Master_Thesis_Brics_Currencies/
│
├── notebooks/                          # Jupyter notebooks — data pipeline and analysis
│   ├── 01_swift_extraction.ipynb       # SWIFT RMB Tracker data extraction
│   ├── 02_data_cleaning.ipynb          # Dataset-by-dataset cleaning (COMPLETE — commit 9eecc92)
│   └── 03_panel_construction.ipynb     # Master panel construction and LCShare proxy (COMPLETE — commit d615189)
│
├── scripts/                            # Python utility scripts
│   ├── extract_swift_v2.py             # SWIFT RMB Tracker data extraction (v2)
│   └── convert_oct22.py                # SWIFT October 2022 format conversion
│
├── outputs/                            # Processed datasets and figures (not tracked in Git)
│   ├── SWIFT_HHI_Annual_Clean.csv      # 13 rows — HHI series 2013–2025
│   ├── SWIFT_RMB_Monthly_Clean.csv     # 86 rows — monthly CNY share 2019–2026
│   ├── BIS_LBS_Clean.csv               # 75 rows — USD/NonUSD share per BRICS country 2010–2024
│   ├── IMF_COFER_Clean.csv             # 16 rows — annual reserve shares 2010–2025
│   ├── IMF_DOTS_Clean_Final.csv        # 840 rows — bilateral trade flows 2010–2024
│   ├── IMF_FX_Volatility_Clean.csv     # 80 rows — annual FX volatility per BRICS currency 2010–2025
│   ├── WorldBank_Macro_Clean.csv       # 75 rows — macro controls per BRICS country 2010–2024
│   ├── Policy_Events_Clean.csv         # 8 rows — DiD treatment events
│   └── Master_Panel_BRICS_2010_2024.csv  # 600 rows, 31 columns — master panel (not tracked)
│
├── DATA_MANIFEST.md                    # Full dataset inventory with citations and gap notes
└── README.md                           # This file
```

> **Note:** Raw data files are stored locally at `/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/` and are not tracked in this repository. Word documents and output CSVs are excluded via `.gitignore`. The canonical record of data collection status is `DATA_MANIFEST.md`.

---

## Data Sources

All eight primary datasets have been collected, cleaned, and integrated into the master panel as of May 2026.

| Dataset | Coverage | Output File | Role in Analysis |
|---------|----------|-------------|-----------------|
| SWIFT Global Currency Tracker | 2013–2025 (HHI); 2019–2026 (monthly CNY) | `SWIFT_HHI_Annual_Clean.csv`; `SWIFT_RMB_Monthly_Clean.csv` | Equation 1 (HHI); LCShare proxy component |
| BIS Locational Banking Statistics | 1977–2025 Q3 | `BIS_LBS_Clean.csv` | LCShare proxy component; financial de-dollarisation measure |
| IMF COFER | 2010–2025 Q3 | `IMF_COFER_Clean.csv` | Equation 1 (reserve concentration) |
| IMF DOTS / IMTS | 2010–2024 | `IMF_DOTS_Clean_Final.csv` | Equation 2 (trade intensity regressor) |
| IMF Exchange Rates | 2010–2026 | `IMF_FX_Volatility_Clean.csv` | Equation 2 (FX volatility control) |
| World Bank WDI | 2010–2024 | `WorldBank_Macro_Clean.csv` | Equation 2 (macro controls) |
| Policy Events Dataset | 2015–2023 | `Policy_Events_Clean.csv` | Equation 3 (DiD treatment assignment) |
| UN Comtrade | 2010–2024 | Validation only — no export | Cross-validation of DOTS (mean deviation: 0.98%) |

### Key Data Notes

- **LCShare dependent variable:** No direct bilateral currency settlement data exists in public sources — confirmed by faculty consultation with Associate Professor Mirco Rubin (HSG, Econometrics). LCShare is constructed as a proxy: `LCShare_i_t = 0.5 × SWIFT_CNY_Share_t + 0.5 × (1 − BIS_USD_Share_i_t)`. This is the field-standard approach given the data constraint and is acknowledged in the methodology chapter.
- **flag_bis_only (2010–2018):** SWIFT monthly CNY data is unavailable before January 2019. For 2010–2018, LCShare uses the BIS component only (full weight), creating a scale break at 2019. A dummy variable `flag_bis_only` is included in the master panel to control for this.
- **SWIFT HHI 2021:** Unavailable from public archives. Treated as a missing observation — not interpolated — given the structural volatility of the COVID-19 recovery period and proximity to the 2022 Russia sanctions shock.
- **SWIFT HHI 2013:** Sourced from a low-resolution Wayback Machine archive image; flagged as approximate (`flag_approximate = True`).
- **UN Comtrade:** Used solely as a cross-validation instrument for DOTS trade figures. Comtrade records trade values in USD — not currency of settlement — and cannot serve as an LCShare source.
- **SWIFT undercounting:** SWIFT data systematically undercounts local currency settlement because CIPS (China) and SPFS (Russia) route payments outside the SWIFT network. Flagged explicitly in the methodology chapter.

---

## Master Panel

The master panel `Master_Panel_BRICS_2010_2024.csv` is the primary input for all three analysis notebooks.

| Property | Value |
|----------|-------|
| Rows | 600 |
| Columns | 31 |
| Unit of observation | Country_i × Country_j × Year |
| BRICS countries (i) | BRA, RUS, IND, CHN, ZAF |
| Counterpart countries (j) | ARE, BRA, CHN, DEU, GBR, IND, JPN, RUS, ZAF |
| Years | 2010–2024 |

**Remaining nulls (all flagged, not imputed):**

| Variable | Null count | Reason |
|----------|-----------|--------|
| `TradeIntensity` | 8 | CHN 2020 export gap (COVID reporting) |
| `BroadMoney_Growth_Pct` | 56 | RUS 2021–2024 + IND 2022–2024 |

---

## Key Empirical Signals Identified During Cleaning

- **Russia de-dollarisation:** BIS USD share falls from 63% (2010) to 18% (2024) — the most dramatic trajectory in the sample. FX volatility peaks at 0.495 in 2022 — largest observation in the dataset.
- **CNY internationalisation arc:** SWIFT share peaks at 4.74% (July 2024), declines to 2.74% (February 2026). COFER share peaks at 2.70% (2021–2022), declines to 1.96% (2025). Post-2022 reversal in both series directly engages the sceptical literature.
- **Russia–China trade surge:** Bilateral trade rises from ~USD 55bn (2019) to ~USD 113bn (2024) post-sanctions — the anchor observation for the DiD estimation.
- **SWIFT HHI spike:** 0.316 in 2022 (vs ~0.300 pre-sanctions) — USD concentration reasserted immediately post-exclusion before partially reverting.

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
- [x] `02_data_cleaning.ipynb` — all 9 datasets cleaned and validated (commit `9eecc92`)
- [x] `03_panel_construction.ipynb` — master panel exported: 600 rows, 31 columns (commit `d615189`)
- [x] LCShare proxy variable constructed (SWIFT + BIS LBS, equal weights baseline)
- [x] 8 DiD treatment dummies and 8 post-period dummies constructed
- [x] Supervisor progress report updated (May 2026)

### In Progress / Upcoming
- [ ] Meeting with HSG methodology advisor (Prof Mirco Rubin) — 4 May 2026 — DiD parallel trends and proxy validation
- [ ] `04_hhi_analysis.ipynb` — Equation 1: HHI concentration analysis and visualisation
- [ ] `05_did_estimation.ipynb` — Equation 3: Difference-in-Differences with event-study plots
- [ ] `06_panel_regression.ipynb` — Equation 2: Fixed-effects panel regression with robustness checks
- [ ] Literature review chapter
- [ ] Methodology chapter
- [ ] Results and discussion chapters
- [ ] Written thesis submission to supervisor (5 June 2026)
- [ ] Oral defense (19–26 June 2026, deadline 30 June 2026)
- [ ] Pre-doctoral application to University of Zurich (UZH)
- [ ] Journal submission (target: post-thesis)

---

## Known Methodological Challenges

| Challenge | Status |
|-----------|--------|
| LCShare proxy relies on indirect sources (SWIFT + BIS LBS) rather than direct settlement data | Acknowledged; field-wide constraint confirmed by HSG faculty consultation |
| flag_bis_only scale break at 2019 — pre/post SWIFT availability creates non-comparable LCShare levels | Controlled via `flag_bis_only` dummy in master panel |
| SWIFT systematically undercounts via CIPS/SPFS | Flagged in methodology; BIS CPMI supplement planned |
| DiD parallel trends assumption — CIPS gradual rollout complicates clean identification | Under review with Prof Mirco Rubin (HSG) — meeting 4 May 2026 |
| Russia sanctions create global spillover effects, complicating clean DiD control group | Under review with Prof Mirco Rubin (HSG) |
| Event 7 (BRICS Johannesburg Summit) treats all 600 panel rows — no untreated control group | Restricted to robustness check only; excluded from main DiD specification |
| Event 6 (Saudi Arabia–China) unconfirmed formal agreement | Flagged (`flag_unconfirmed = True`); excluded from main specification |
| HHI measure is aggregate — may mask bilateral heterogeneity | Addressed via extension to individual BRICS currencies |
| CNY COFER data only available from 2016-Q4 | Known institutional fact; stated in methodology; not backfilled |

---

## Timeline

| Milestone | Date |
|-----------|------|
| Data collection complete | 22 March 2026 ✓ |
| Data cleaning and panel construction complete | May 2026 ✓ |
| HSG advisor meeting (Prof Mirco Rubin, Meeting 3) | 4 May 2026 |
| Analysis notebooks complete | May 2026 |
| Written thesis submission to supervisor | 5 June 2026 |
| Oral defense | 19–26 June 2026 |
| Defense deadline | 30 June 2026 |

---

## Data Citations

Bank for International Settlements (2026), Locational banking statistics, BIS WS_LBS_D_PUB 1.0 (data set), https://data.bis.org/search, accessed 18 March 2026.

International Monetary Fund (2026), Currency Composition of Official Foreign Exchange Reserves (COFER), IMF.STA:COFER(7.0.1), https://data.imf.org, accessed 19 March 2026.

International Monetary Fund (2026), International Trade in Goods by Partner Country (IMTS), IMF.STA:IMTS(1.0.0), https://data.imf.org, accessed 19 March 2026.

International Monetary Fund (2026), Exchange Rates (ER), IMF.STA:ER(4.0.1), https://data.imf.org, accessed 19 March 2026.

SWIFT (2026), Global Currency Tracker (formerly RMB Tracker), https://www.swift.com/our-solutions/compliance-and-shared-services/business-intelligence/renminbi/rmb-tracker, accessed March 2026.

United Nations (2026), UN Comtrade Database, https://comtradeplus.un.org, accessed 22 March 2026.

World Bank (2026), World Development Indicators, https://databank.worldbank.org, accessed 19 March 2026.

---

## Contact

**Aadhitya Tejaswin Prakash Sridevi**  
Master in Management (Business Management), EDHEC Business School  
Full-Year Exchange in Quantitative Economics, University of St. Gallen (HSG)  
GitHub: [Aadhi0105](https://github.com/Aadhi0105)

---

*Last updated: 3 May 2026*