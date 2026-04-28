
---

## DVA-Focused Portfolio Case Study

> This section converts the capstone into a portfolio-ready case study for Data Visualisation & Analytics (DVA).

---

### Problem Statement & Stakeholder Context

Global terrorism has evolved significantly over the past five decades — shifting geographically, tactically, and ideologically. This project addresses the question:

> **Where, when, and why do terrorist attacks occur — and what patterns can data reveal?**

Stakeholders include policy analysts, security researchers, and academic institutions seeking data-driven insight into conflict trends to inform prevention strategies and resource allocation.

---

### Dataset Source & Scope

| Property | Detail |
|---|---|
| Source | [Kaggle — Global Terrorism Database](https://www.kaggle.com/) |
| Original maintainer | START Center, University of Maryland |
| Coverage | 1970 – 2017 |
| Raw size | 181,691 incidents × 135 columns |
| Cleaned size | 34,268 rows × 9 columns |

---

### Cleaning & Transformation Summary

| Step | Action |
|---|---|
| Column selection | Reduced 135 columns to 9 relevant features |
| Renaming | Mapped raw column names to clean readable labels |
| Missing values | Dropped all rows with any `NaN` or empty string |
| Unknown placeholders | Replaced `'Unknown'` strings in `City` and `Reason` with `NaN` before dropping |
| Feature engineering | Added `Month_Name`, `Decade`, `Operating_Mode`, `Incident_Scale` |

---

### KPI Framework

| KPI | Description |
|---|---|
| Total Incidents | Count of recorded terrorist attacks |
| Attack Growth Rate | Year-over-year % change in incident count |
| Regional Concentration | % share of global attacks per region per decade |
| Siege Rate | % of attacks lasting >24 hours by region |
| Individual Actor Rate | % of attacks carried out by lone actors |
| Motive Coverage | % of incidents with a documented motive |

---

### Key Insights

1. **Conflict has migrated east** — Western Europe and South America dominated incidents in the 1970s–1990s. By the 2000s, South Asia and MENA account for over 60% of all attacks.

2. **Statistically significant upward trend** — Kendall Tau test confirms a monotonic increase in attack frequency across the full 1970–2017 period (p < 0.05).

3. **South Asia leads in siege tactics** — South Asia has the highest propensity for extended-duration (>24h) attacks, suggesting well-organised, logistically capable groups.

4. **Region and attack type are not independent** — Chi-Square tests confirm significant associations between region and both Duration and Individual actor flags (p < 0.05).

5. **Three dominant motive clusters** — NLP topic modeling (NMF) on the `Reason` field reveals recurring themes: self-determination, retaliation against military operations, and political interference.

---

### Tableau Dashboard

| Item | Detail |
|---|---|
| Dashboard link | _(to be added)_ |
| Screenshots | _(to be added)_ |

---

### Recommendations & Expected Impact

| Recommendation | Expected Impact |
|---|---|
| _(to be added)_ | _(to be added)_ |

---

### Portfolio Deliverable

A write-up of this case study is available at:

> _(Add link to your portfolio site, Notion page, or PDF case study here)_

This repository serves as the technical backbone — all code, notebooks, and data pipeline are fully reproducible.
