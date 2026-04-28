import os
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH  = os.path.join(BASE_DIR, "data", "raw", "globalterrorismdb_0718dist.csv")
OUT_PATH  = os.path.join(BASE_DIR, "data", "processed", "gtd_cleaned.csv")

# ── Column mapping (raw → clean) ───────────────────────────────────────────────
COLUMNS = {
    "iyear"       : "Year",
    "imonth"      : "Month",
    "extended"    : "Duration",
    "country_txt" : "Country",
    "region_txt"  : "Region",
    "city"        : "City",
    "crit1"       : "Crime",
    "motive"      : "Reason",
    "individual"  : "Individual",
}


# ── 1. Extract ─────────────────────────────────────────────────────────────────
def extract(path: str) -> pd.DataFrame:
    """Load the raw GTD CSV file."""
    print(f"[Extract] Reading: {path}")
    df = pd.read_csv(path, encoding="latin-1", low_memory=False)
    print(f"[Extract] Loaded {df.shape[0]:,} rows × {df.shape[1]} columns")
    return df


# ── 2. Transform ───────────────────────────────────────────────────────────────
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Select, rename, and clean the relevant columns."""

    # --- Select & rename ---
    df = df[list(COLUMNS.keys())].rename(columns=COLUMNS)
    print(f"[Transform] After column selection: {df.shape}")

    # --- Replace empty strings and 'Unknown' placeholders with NaN ---
    df.replace("", pd.NA, inplace=True)
    df["City"]   = df["City"].str.strip().replace("Unknown", pd.NA)
    df["Reason"] = df["Reason"].str.strip().replace("Unknown", pd.NA)

    # --- Drop all rows with any missing value ---
    before = len(df)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(f"[Transform] Dropped {before - len(df):,} rows with missing values")
    print(f"[Transform] Final shape: {df.shape}")

    # --- Validate: no nulls remain ---
    null_counts = df.isnull().sum()
    if null_counts.any():
        print("[Transform] WARNING — nulls still present:")
        print(null_counts[null_counts > 0])
    else:
        print("[Transform] Validation passed — no missing values")

    return df


# ── 3. Load ────────────────────────────────────────────────────────────────────
def load(df: pd.DataFrame, path: str) -> None:
    """Save the cleaned DataFrame to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[Load] Saved {len(df):,} rows to: {path}")


# ── Main ───────────────────────────────────────────────────────────────────────
def run_pipeline():
    print("=" * 55)
    print("  GoldDigger ETL Pipeline")
    print("=" * 55)

    df = extract(RAW_PATH)
    df = transform(df)
    load(df, OUT_PATH)

    print("=" * 55)
    print("  Pipeline complete.")
    print("=" * 55)


if __name__ == "__main__":
    run_pipeline()
