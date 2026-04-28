# DVA-Oriented Resume — GoldDigger: Echoes of Conflict

Use this as a reference when updating your resume to reflect this capstone project.

---

## Suggested Resume Bullet (Copy & Adapt)

> Built an end-to-end data analytics capstone on global terrorism (public safety sector) using Python, Jupyter, and GitHub; ingested and cleaned 181,691 raw records down to 34,268 analysis-ready rows, engineered a 6-KPI framework, applied statistical hypothesis testing (Chi-Square, Kruskal-Wallis, Kendall Tau), and delivered dashboard-backed insights identifying a 50-year eastward migration of conflict concentration.

---

## Resume Points by Contribution Area

### ETL & Data Engineering
- Built a standalone ETL pipeline (`etl_pipeline.py`) in Python that extracts, transforms, and loads the Global Terrorism Database — reducing 181,691 raw records to 34,268 clean rows with zero missing values
- Reduced 135 raw columns to 9 analysis-ready features through targeted column selection, renaming, and null-handling logic
- Automated data validation step to confirm zero nulls post-transform before writing output

### Exploratory Data Analysis (EDA)
- Conducted temporal, geographic, and categorical EDA across 34,268 terrorism incidents spanning 1970–2017 using Python (pandas, matplotlib, seaborn)
- Identified a peak of ~16,900 incidents in 2014 and confirmed a statistically significant long-term upward trend via Kendall Tau test
- Visualised attack distributions across 12 world regions, 154 countries, and 10,836 unique cities

### Statistical Analysis
- Applied 6 hypothesis tests (Chi-Square, Kruskal-Wallis, Kendall Tau) to quantify relationships between region, attack duration, individual actors, and criminal classification — all returning p < 0.05
- Used Z-score outlier detection to identify countries with statistically anomalous attack frequencies
- Computed descriptive statistics (skewness, kurtosis, variance) across all numeric features

### KPI Design
- Designed a 6-KPI framework covering: total incidents, YoY growth rate, regional concentration, siege rate, individual actor rate, and motive coverage
- Engineered 4 new analytical features: `Month_Name`, `Decade`, `Operating_Mode`, `Incident_Scale`

### NLP & Advanced Analytics
- Applied NMF topic modeling (scikit-learn) to 34,268 free-text motive entries, extracting 3 dominant conflict-driver themes: self-determination, retaliation, and political interference
- Built a decadal regional heatmap confirming a major shift in global conflict concentration from Western Europe/South America (1970–1990) to South Asia/MENA (2000–present)

### Dashboarding & Reporting
- Tableau dashboard: _(add link after publishing to Tableau Public)_
- GitHub repository: _(add link)_

---

## Tools Used

| Tool | Purpose |
|---|---|
| Python 3 | ETL, EDA, statistical analysis, NLP |
| pandas, numpy | Data manipulation |
| matplotlib, seaborn | Visualisation |
| scipy | Hypothesis testing |
| scikit-learn | NMF topic modeling |
| Jupyter Notebook | Interactive analysis |
| Tableau Public | Dashboard & visualisation |
| GitHub | Version control & portfolio hosting |

---

## Project Metadata

| Field | Value |
|---|---|
| Project title | GoldDigger: Echoes of Conflict |
| Sector | Public Safety / Security Analytics |
| Problem | Identifying global terrorism patterns across 50 years of incident data |
| Dataset | Global Terrorism Database (GTD) via Kaggle — 181,691 incidents |
| Cleaned dataset | 34,268 rows × 9 columns |
| Date | _(add year)_ |
