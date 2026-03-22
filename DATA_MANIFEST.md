# Data Manifest — BRICS Currencies Thesis

## Local Data Path
/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/

## Datasets

| Dataset | Folder | Files | Period | Citation |
|---------|--------|-------|--------|----------|
| BIS Locational Banking Statistics | BIS Dataset | 5 CSV files (one per BRICS country) | 1977–2025 Q3 | BIS WS_LBS_D_PUB 1.0, accessed 18 Mar 2026 |
| SWIFT Global Currency Tracker | SWIFT Dataset | 42 PDFs + RMB_Evolution_2019_2026.csv + SWIFT_HHI_Annual.xlsx | 2019–2026 | SWIFT Global Currency Tracker, accessed Mar 2026 |
| IMF COFER | IMF Dataset | IMF_COFER_Final_2010_2025.csv | 2010–2025 Q3 | IMF.STA:COFER(7.0.1), accessed 19 Mar 2026 |
| IMF DOTS/IMTS | IMF Dataset | IMF_DOTS_Clean_2010_2024.csv | 2010–2024 | IMF.STA:IMTS(1.0.0), accessed 19 Mar 2026 |
| IMF Exchange Rates | IMF Dataset | IMF_FX_Monthly_2010_2026.csv + IMF_FX_Volatility_Annual_2010_2025.csv | 2010–2026 | IMF.STA:ER(4.0.1), accessed 19 Mar 2026 |
| World Bank WDI | WBG Dataset | WorldBank_Macro_Controls_2010_2024.csv | 2010–2024 | World Bank WDI, accessed 19 Mar 2026 |
| Policy Events | Events Dataset | Policy_Events_Dataset.xlsx | 2015–2023 | Self-constructed from primary sources |
| UN Comtrade | UN Comtrade Dataset | UN_Comtrade_BRICS_2010_2024.csv | 2010–2024 | UN Comtrade Database, accessed 22 Mar 2026 |

## Cross-Validation Result
Comtrade vs DOTS comparison for 2023 exports confirms deviations below 1%
for all major BRICS bilateral pairs. DOTS used as primary source.
Largest discrepancy: CHN→IND at 0.80% — within normal statistical tolerance.

## Data Gaps
- SWIFT public archive starts October 2022 only — pre-2022 data from rolling charts
- CNY in COFER only from 2016-Q4 — China joined SDR basket October 2016
- Russia broad money growth missing 2021–2024 — sanctions reporting restriction
- India broad money growth missing 2022–2024 — World Bank reporting lag
- China DOTS exports missing 2020 — COVID reporting gap
- Pre-2019 SWIFT HHI data — pending supplementation from BIS quarterly reviews

## Status
All primary data sources complete as of 22 March 2026.
Remaining: Pre-2019 HHI supplementation from BIS quarterly reviews.