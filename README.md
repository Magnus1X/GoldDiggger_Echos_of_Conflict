# GoldDigger: Echoes of Conflict

An end-to-end data analysis project exploring global terrorism patterns using the **Global Terrorism Database (GTD) 1970–2017**.

---

## Project Overview

This project investigates trends, geographic distributions, attack types, and casualty patterns in terrorist incidents recorded over nearly five decades. The analysis pipeline covers data extraction, cleaning, exploratory data analysis (EDA), and statistical analysis.

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
