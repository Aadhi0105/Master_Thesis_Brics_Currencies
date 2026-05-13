# BRICS Currencies and Global Monetary Fragmentation
### Master's Thesis — Empirical Analysis of Local Currency Settlement in International Trade (2010–2025)

**Author:** Aadhitya Tejaswin Prakash Sridevi  
**Programme:** Master in Management (Business Management), EDHEC Business School  
**Exchange:** University of St. Gallen (HSG) — Full-Year Exchange, Quantitative Economics  
**Supervisor:** EDHEC Business School  
**Status:** All empirical notebooks complete — thesis writing phase (May 2026)

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
An event-study design estimating the causal effect of eight discrete policy events on local currency settlement. The strongest identification comes from the Russia SWIFT exclusion (February 2022), which provides a large, discrete, and well-documented treatment. Additional events include the CIPS Phase 1 and Phase 2 launches, the India-Russia Rupee Framework, the Brazil-China RMB Agreement, and the BRICS Johannesburg Summit Declaration (2023).

---

## Repository Structure

```
Master_Thesis_Brics_Currencies/
│
├── notebooks/                          # Jupyter notebooks — data pipeline and analysis
│   ├── 01_swift_extraction.ipynb       # SWIFT RMB Tracker data extraction
│   ├── 02_data_cleaning.ipynb          # Dataset-by-dataset cleaning (COMPLETE — commit 9eecc92)
│   ├── 03_panel_construction.ipynb     # Master panel construction and LCShare proxy (COMPLETE — commit d615189)
│   ├── 04_hhi_analysis.ipynb           # Equation 1: HHI concentration analysis (COMPLETE)
│   ├── 05_did_estimation.ipynb         # Equation 3: DiD estimation (COMPLETE — commit 7c6b813)
│   └── 06_panel_regression.ipynb      # Equation 2: Fixed-effects panel regression (COMPLETE — commit 613942d)
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
│   ├── Master_Panel_BRICS_2010_2024.csv  # 600 rows, 31 columns — master panel (not tracked)
│   ├── panel_main_results.csv          # Equation 2 main regression results — Specs 1–4
│   ├── panel_robustness.csv            # Equation 2 robustness checks
│   ├── panel_descriptive_stats.csv     # Equation 2 descriptive statistics
│   ├── did_main_results.csv            # Equation 3 DiD main results — Specs 1–4
│   ├── did_robustness.csv              # Equation 3 robustness checks
│   └── did_heterogeneity.csv           # Equation 3 heterogeneity analysis
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
- **flag_bis_only (2010–2018):** SWIFT monthly CNY data is unavailable before January 2019. For 2010–2018, LCShare uses the BIS component only (full weight), creating a scale break at 2019. A dummy variable `flag_bis_only` is included in the master panel to control for this discontinuity in all specifications.
- **SWIFT HHI 2021:** Unavailable from public archives. Treated as a missing observation — not interpolated — given the structural volatility of the COVID-19 recovery period and proximity to the 2022 Russia sanctions shock.
- **SWIFT HHI 2013:** Sourced from a low-resolution Wayback Machine archive image; flagged as approximate (`flag_approximate = True`).
- **UN Comtrade:** Used solely as a cross-validation instrument for DOTS trade figures. Comtrade records trade values in USD — not currency of settlement — and cannot serve as an LCShare source.
- **SWIFT undercounting:** SWIFT data systematically undercounts local currency settlement because CIPS (China) and SPFS (Russia) route payments outside the SWIFT network. All LCShare estimates are conservative lower bounds. Flagged explicitly in the methodology chapter.

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

## Key Empirical Findings

All three empirical equations are complete. The findings are summarised below by equation. Full results are documented in the Empirical Results Document and in the output CSVs.

### Equation 1 — HHI Concentration Analysis

The central finding is a divergence between the payments and reserve dimensions following the Russia SWIFT exclusion of February 2022. The SWIFT HHI spiked from approximately 0.300 in 2020 to **0.316 in 2022** — the sample maximum — as USD concentration in global payment flows increased in the year of the sanctions. The COFER HHI continued its monotonic decline through 2022 without any reversal, reflecting the different adjustment speeds of the transactional and store-of-value roles of the dollar.

Key findings:

- **SWIFT HHI range:** 0.291 (2013) to 0.316 (2022). Dollar concentration reasserted post-sanctions before partially reverting.
- **COFER USD share:** declined from 61.8% (2010) to 56.9% (2025-Q3). Gradual, uninterrupted reserve diversification over 15 years.
- **CNY COFER:** peaked at 2.70% (2021–2022), declined to 1.96% (2025). CNY reserve internationalisation has reversed.
- **CNY SWIFT:** peaked at 4.74% (July 2024), declined to 2.74% (February 2026). CNY payments internationalisation has also peaked.
- **Post-2022 compositional shift in SWIFT:** the primary beneficiary was USD (+4 pp), not CNY (+1.6 pp), while EUR lost over 6 pp. The network externality advantage of the dollar absorbed EUR's loss, not the renminbi.
- **BRL, RUB, INR:** absent from the top 20 global payment currencies throughout the sample. ZAR at 0.32% only. Non-CNY BRICS currencies have achieved no measurable internationalisation in global payment flows.

**Bottom line:** Dollar dominance in payment flows strengthened after the largest sanctions shock in modern financial history. CNY internationalisation has demonstrated a ceiling in both the payments and reserve dimensions. The DCP prediction of system-level dollar resilience is confirmed.

---

### Equation 2 — Fixed-Effects Panel Regression

The regression identifies the within-pair, time-varying structural determinants of LCShare across four specifications (N = 592 in the preferred Spec 2; N = 536 in the full-controls Spec 3). All specifications use two-way fixed effects (pair + year) with standard errors clustered at the country-pair level.

**Primary findings:**

| Variable | Spec 1 | Spec 2 | Spec 3 | Spec 4 | Assessment |
|---|---|---|---|---|---|
| FX Volatility | −21.2*** | −14.2** | −47.5*** | −6.4*** | Dominant, robust — strengthens ex-Russia |
| Trade Intensity | −41.3 | −27.0 | −58.0 | +2.9 | Precise null throughout — invoicing inertia |
| Inflation | — | −0.75** | −0.71*** | −0.21* | Robust — consistent sign all specs |
| Broad Money Growth | — | — | −0.71*** | — | Consistent with monetary instability channel |
| log(GDP) | — | −11.5 | +23.2** | +8.8*** | Russia-sensitive — interpret with caution |
| Trade Openness | — | −0.51* | +1.32*** | −0.15*** | Unstable — Spec 4 most reliable |
| R² (within) | 0.021 | 0.065 | 0.219 | 0.410 | |

*Significance: \*\*\* p<0.001  \*\* p<0.01  \* p<0.05*

**Key results:**

- **FX Volatility** is the dominant and most robust driver of LCShare. The negative coefficient is significant at p < 0.001 in three of four specifications, stable in sign throughout, and strengthens to −96.6 when Russia pairs are excluded — confirming the result is not a Russia outlier artefact. Higher currency volatility suppresses local currency settlement. This is the voluntary channel described by DCP: parties avoid volatile currencies for invoicing.
- **Trade Intensity** produces a precise null in every specification. Within-pair changes in bilateral trade volumes over 2010–2024 do not translate into measurable shifts in local currency settlement. DCP invoicing inertia dominates the bilateral trade depth channel.
- **Inflation and Broad Money Growth** are both negative and significant, confirming that monetary instability in any form suppresses local currency settlement.
- **The Russia 2022 tension:** Russia's 2022 FX volatility (0.495, four times the sample mean) should under Equation 2 suppress LCShare. Yet Equation 3 finds LCShare increased by 19.3 pp. These results are not contradictory — Equation 2 captures the voluntary channel (parties choose the dollar when currencies are volatile); Equation 3 captures the forced channel (parties have no choice when dollar access is removed). They operate at different margins.

**Bottom line:** The preconditions for lasting local currency internationalisation are macroeconomic — monetary credibility and exchange rate stability — not simply bilateral trade volumes. BRICS currencies need to be stable before trade depth can translate into settlement currency shifts.

---

### Equation 3 — Difference-in-Differences

The DiD estimates the causal effect of the Russia SWIFT exclusion (February 2022) on LCShare in Russia bilateral corridors, using non-Russia BRICS pairs as the control group. All specifications use two-way fixed effects (pair + year) with standard errors clustered at the country-pair level.

**Main results (Event 3 — Russia SWIFT Exclusion):**

| Specification | δ (pp) | SE | p-value | N |
|---|---|---|---|---|
| Spec 1 — no controls | 10.442 | 1.595 | <0.001*** | 600 |
| Spec 2 — + flag_bis_only | 10.442 | 1.597 | <0.001*** | 600 |
| Spec 3 — full controls (HEADLINE) | **19.296** | **3.358** | **<0.001*** | **592** |
| Spec 4 — multi-event | 20.149 | 3.467 | <0.001*** | 592 |

*Treated observations: 24 (8 Russia pairs × 3 post-event years: 2022, 2023, 2024)*

**Key results:**

- **Headline (Spec 3):** The Russia SWIFT exclusion caused a **19.3 percentage point increase** in local currency settlement share in Russia-involved bilateral corridors post-2022 (95% CI: [12.5, 26.1]). This represents a shift of more than half a standard deviation in LCShare and is durable across three post-event years.
- **The jump from Spec 1 to Spec 3** (10.4 → 19.3 pp) is not instability — it occurs because Russia's post-2022 economic deterioration (GDP contraction, inflation, trade collapse) was a headwind to LCShare. Controlling for these headwinds reveals the larger underlying structural shift toward local currency channels.
- **Specs 1 and 2 are identical** (10.442 pp), confirming that the 2019 LCShare scale break (`flag_bis_only`) did not inflate the baseline DiD estimate.
- **Heterogeneity:** The treatment effect estimated on the seven non-China Russia pairs alone is **19.1 pp** — virtually identical to the pooled 19.3 pp. The headline finding is not a story of Russia rerouting trade through China's CIPS infrastructure. It is generalised de-dollarisation across Russia's entire bilateral trade network, driven by the structural constraint that SWIFT exclusion applies uniformly to all dollar-denominated international banking regardless of counterpart.
- **Event study:** The treatment effect builds over time — near zero in 2022 (β = 0.204, p = 0.163), significant and growing in 2023 (β = 1.365, p < 0.001) and 2024 (β = 3.154, p < 0.001) — consistent with CIPS transaction capacity expanding by approximately 75% between 2022 and 2024.
- **Caveats:** The placebo test (fake treatment year 2019) is significant at 8.1 pp, indicating Russia pairs were elevated above control pairs before 2022. Pre-trends plots confirm this is a stable level difference rather than a diverging trend. The parallel trends assumption holds over the 2019–2021 comparable window. This limitation is documented explicitly in the methodology chapter.

**Bottom line:** Forced de-dollarisation — when dollar access is structurally removed — is real, quantifiable, and broad-based. The 19.3 pp treatment effect coexists with Equation 1's finding of aggregate USD reassertion because corridor-level forced rerouting and system-level dollar concentration operate at different levels of the global currency system simultaneously.

---

### Cross-Equation Synthesis

The three equations analyse the same phenomenon at three levels and their findings are coherent rather than contradictory:

| Level | Equation | Core Finding |
|---|---|---|
| System | Equation 1 (HHI) | USD dominance strengthened post-2022 in aggregate payment flows. CNY peaked and reversed in both payments and reserves. |
| Structural | Equation 2 (Panel) | FX volatility dominates within pairs. Trade intensity produces a precise null. Monetary stability is the precondition for local currency settlement. |
| Corridor | Equation 3 (DiD) | Forced de-dollarisation is real. Russia SWIFT exclusion caused +19.3 pp in Russia bilateral corridors — broad-based, not China-specific. |

The dollar is simultaneously resilient at the system level, conditionally suppressible at the structural level by monetary instability, and breakable at the corridor level under sufficient geopolitical coercion — but only when that coercion removes dollar access entirely rather than merely creating incentives to find alternatives.

---

## Known Methodological Challenges

| Challenge | Status |
|-----------|--------|
| LCShare proxy relies on indirect sources (SWIFT + BIS LBS) rather than direct settlement data | Acknowledged; field-wide constraint confirmed by HSG faculty consultation. All estimates are conservative lower bounds. |
| flag_bis_only scale break at 2019 — pre/post SWIFT availability creates non-comparable LCShare levels | Controlled via `flag_bis_only` dummy. Confirmed non-binding by Spec 4 post-2019 subsample. |
| SWIFT systematically undercounts via CIPS/SPFS | Flagged in methodology; all coefficient estimates downward-biased. |
| DiD parallel trends assumption — pre-trend detected at k=−3, k=−2 | Documented; stable level difference, not diverging trend. Full causal interpretation qualified accordingly. |
| Event 7 (BRICS Johannesburg Summit) treats all 600 panel rows — no untreated control group | Restricted to robustness check only; excluded from main DiD specification. |
| Event 6 (Saudi Arabia–China) unconfirmed formal agreement | Flagged (`flag_unconfirmed = True`); Treat = 0 for all rows. Excluded from all specifications. |
| BroadMoney_Growth_Pct excluded from DiD controls | RUS 2021–2024 nulls would drop all post-treatment Russia observations from the estimation sample. Excluded by design. |
| 24 treated observations in DiD | Wide confidence intervals acknowledged. Result significant despite low statistical power. |
| HHI measure is aggregate — may mask bilateral heterogeneity | Addressed via heterogeneity analysis in Equation 3 and individual-pair decomposition. |
| CNY COFER data only available from 2016-Q4 | Known institutional fact; stated in methodology; not backfilled. |

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

*Last updated: May 2026*