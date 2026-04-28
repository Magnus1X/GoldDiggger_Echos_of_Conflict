# GoldDigger: Echoes of Conflict

An end-to-end data analysis project exploring global terrorism patterns using the **Global Terrorism Database (GTD) 1970–2017**.

---

## Project Overview

This project investigates trends, geographic distributions, attack types, and casualty patterns in terrorist incidents recorded over nearly five decades. The analysis pipeline covers data extraction, cleaning, exploratory data analysis (EDA), and statistical analysis.

## Results & Key Findings
- Peak year of global terrorism: 2014 (~16,900 incidents)
- Most impacted region: Middle East & North Africa (MENA)
- Most impacted country: Iraq
- Most common attack type: Bombing/Explosion
- Average casualties per incident: 2.3
- Total incidents processed: 34,268
- Top terrorist group: Taliban

## Tableau Dashboard
[Link will be added after publishing to Tableau Public]

---

## Dataset

- **Source:** Global Terrorism Database (GTD)
- **File:** `data/raw/globalterrorismdb_0718dist.csv`
- **Coverage:** 1970–2017
- **Size:** 181,691 incidents × 135 columns
- **Encoding:** `latin-1`

---

## Project Structure

```
GoldDiggger_Echos_of_Conflict/
├── data/
│   ├── raw/                  # Raw GTD CSV file
│   └── processed/            # Cleaned dataset (gtd_cleaned.csv)
├── docs/
│   └── data_dictionary.md    # Column descriptions
├── Notebooks/
│   ├── 01_extraction.ipynb   # Data loading and initial exploration
│   ├── 02_cleaning.ipynb     # Data cleaning and feature engineering
│   ├── 03_eda.ipynb          # Exploratory data analysis with visualizations
│   └── 04_statistical_analysis.ipynb  # Statistical analysis
├── scripts/
│   └── etl_pipeline.py       # ETL pipeline script
├── requirements.txt
└── README.md
```

---

## Notebooks

| Notebook | Description |
|---|---|
| `01_extraction.ipynb` | Loads raw GTD data, inspects shape, schema, data types, missing values, and key distributions |
| `02_cleaning.ipynb` | Filters, renames, and transforms columns; handles missing values; outputs cleaned CSV |
| `03_eda.ipynb` | Temporal, geographic, and categorical visualizations on the cleaned dataset |
| `04_statistical_analysis.ipynb` | Statistical tests and deeper analysis |

---

## Cleaned Dataset Schema

After cleaning, the dataset contains **34,268 rows × 9 columns**:

| Column | Type | Description |
|---|---|---|
| `Year` | int | Year of the incident |
| `Month` | int | Month of the incident |
| `Duration` | int | Whether the incident was extended (0/1) |
| `Country` | str | Country where the attack occurred |
| `Region` | str | World region |
| `City` | str | City where the attack occurred |
| `Crime` | int | Whether the incident meets terrorism criteria (0/1) |
| `Reason` | str | Stated motive for the attack |
| `Individual` | int | Whether the perpetrator acted alone (0/1) |

---

## Key Findings

### Temporal Trends
- Attacks increased dramatically from the 1970s through the 2010s, peaking around **2014 (~16,900 incidents)**.
- A notable data gap exists for **1993** in the original GTD.

### Top Countries by Attacks
| Country | Incidents |
|---|---|
| Iraq | 24,636 |
| Pakistan | 14,368 |
| Afghanistan | 12,731 |
| India | 11,960 |
| Colombia | 8,306 |

### Top Regions
| Region | Incidents |
|---|---|
| Middle East & North Africa | 50,474 |
| South Asia | 44,974 |
| South America | 18,978 |
| Sub-Saharan Africa | 17,550 |
| Western Europe | 16,639 |

### Attack Types
| Type | Count |
|---|---|
| Bombing/Explosion | 88,255 |
| Armed Assault | 42,669 |
| Assassination | 19,312 |
| Hostage Taking (Kidnapping) | 11,158 |

### Casualties (Raw Dataset)
- **Total killed:** 411,868
- **Average killed per incident:** 2.4
- **Maximum killed in a single incident:** 1,570
- **Total wounded:** 523,869

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Requirements

```
numpy
pandas
scikit-learn
matplotlib
seaborn
```

---

## Usage

1. Place the raw GTD CSV file at `data/raw/globalterrorismdb_0718dist.csv`.
2. Run the notebooks in order:
   ```
   01_extraction.ipynb → 02_cleaning.ipynb → 03_eda.ipynb → 04_statistical_analysis.ipynb
   ```
3. Alternatively, run the ETL pipeline script:
   ```bash
   python scripts/etl_pipeline.py
   ```

---

## License

This project is for educational and research purposes. The Global Terrorism Database is maintained by the National Consortium for the Study of Terrorism and Responses to Terrorism (START) at the University of Maryland.

---

## ETL Pipeline Script

`scripts/etl_pipeline.py` replicates the full cleaning pipeline from the notebooks as a single runnable script — no Jupyter required.

### What it does

| Stage | Action |
|---|---|
| **Extract** | Reads `data/raw/globalterrorismdb_0718dist.csv` with `latin-1` encoding |
| **Transform** | Selects and renames the 9 relevant columns, replaces empty strings and `'Unknown'` placeholders with `NaN`, drops all rows with any missing value, resets the index |
| **Load** | Saves the cleaned DataFrame to `data/processed/gtd_cleaned.csv` |

### Output

```
=======================================================
  GoldDigger ETL Pipeline
=======================================================
[Extract] Reading: .../data/raw/globalterrorismdb_0718dist.csv
[Extract] Loaded 181,691 rows × 135 columns
[Transform] After column selection: (181691, 9)
[Transform] Dropped 147,423 rows with missing values
[Transform] Final shape: (34268, 9)
[Transform] Validation passed — no missing values
[Load] Saved 34,268 rows to: .../data/processed/gtd_cleaned.csv
=======================================================
  Pipeline complete.
=======================================================
```

---

## Notebook 5 — Final Load & Analytical Insights

`05_final_load_prep.ipynb` is the culmination of the pipeline. It loads the cleaned data, engineers new features, and produces three advanced insight layers.

**Data lineage:** Raw (N1) → Cleaned (N2) → Explored (N3) → Tested (N4) → Insights (N5)

### Feature Engineering

| New Column | Description |
|---|---|
| `Month_Name` | Human-readable month label (Jan–Dec) |
| `Decade` | Temporal bucket (1970, 1980, …, 2010) |
| `Operating_Mode` | `Organized Group` or `Individual Actor` |
| `Incident_Scale` | `Immediate (<24h)` or `Siege/Extended (>24h)` |

### Insight Layers

**Layer 1 — Geography of Risk**
A decadal heatmap showing how the regional share of global incidents has shifted over 50 years. Confirms a major migration of conflict concentration from Western Europe and South America (1970–1990) to South Asia and MENA (2000–present).

**Layer 2 — Tactics & Patterns**
Bar chart of siege-tactic propensity (extended duration attacks) by region. South Asia shows not only high volume but also a higher rate of siege tactics, implying well-coordinated logistical structures.

**Layer 3 — Root Motives (NLP)**
NMF topic modeling on the `Reason` free-text field extracts four recurring motive themes:
- Self-determination (autonomy / independence)
- Retaliatory action (protesting military operations)
- Political influence (interfering with elections)

### Output

Exports an enriched dataset to `data/processed/gtd_final_insights.csv` with the new feature columns appended.

### Future Directions

- **Sentiment Analysis** — apply VADER or TextBlob to motives to gauge emotional intensity
- **Geospatial Clustering** — use coordinate data with DBSCAN or K-Means to identify non-administrative conflict zones
- **Time-Series Forecasting** — ARIMA-based attack frequency predictions
