import os
import time
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH  = os.path.join(BASE_DIR, "data", "raw", "globalterrorismdb_0718dist.csv")
OUT_PATH  = os.path.join(BASE_DIR, "data", "processed", "gtd_cleaned.csv")

def extract(path: str) -> pd.DataFrame:
    print("Step 1: Load raw CSV from data/raw/")
    try:
        df = pd.read_csv(path, encoding="latin-1", low_memory=False)
    except FileNotFoundError:
        print(f"Error: Could not find raw file at {path}")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
        
    print(f"Step 2: Print shape of raw data: {df.shape}")
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("Step 3: Drop columns where >60% values are null")
    threshold = 0.6 * len(df)
    df = df.dropna(thresh=threshold, axis=1)

    print("Step 4: Keep only these 9 key columns")
    keep_cols = ['eventid', 'iyear', 'country_txt', 'region_txt', 'attacktype1_txt', 
                 'targtype1_txt', 'gname', 'nkill', 'nwound']
    
    # We ensure we only keep these columns if they exist.
    available_cols = [c for c in keep_cols if c in df.columns]
    df = df[available_cols].copy()
    
    print("Step 5: Rename columns")
    rename_map = {
        'eventid': 'event_id',
        'iyear': 'year',
        'country_txt': 'country',
        'region_txt': 'region',
        'attacktype1_txt': 'attack_type',
        'targtype1_txt': 'target_type',
        'gname': 'group_name',
        'nkill': 'killed',
        'nwound': 'wounded'
    }
    df.rename(columns=rename_map, inplace=True)
    
    print("Step 6: Drop rows where year, country, region, or attack_type is null")
    req_cols = ['year', 'country', 'region', 'attack_type']
    # Check if these columns exist first
    existing_req = [c for c in req_cols if c in df.columns]
    df.dropna(subset=existing_req, inplace=True)
    
    print("Step 7: Fill null killed and wounded with 0")
    if 'killed' in df.columns:
        df['killed'].fillna(0, inplace=True)
    if 'wounded' in df.columns:
        df['wounded'].fillna(0, inplace=True)
        
    print("Step 8: Add a 'casualties' column = killed + wounded")
    if 'killed' in df.columns and 'wounded' in df.columns:
        df['casualties'] = df['killed'] + df['wounded']
        
    return df

def load(df: pd.DataFrame, path: str) -> None:
    print("Step 9: Save cleaned data to data/processed/gtd_cleaned.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    
    print(f"Step 10: Print final shape and first 5 rows")
    print(f"Final shape: {df.shape}")
    print("First 5 rows:")
    print(df.head().to_string())

def run_pipeline():
    start_time = time.time()
    print("=" * 55)
    print("  GoldDigger ETL Pipeline")
    print("=" * 55)

    df = extract(RAW_PATH)
    if df is not None:
        df = transform(df)
        load(df, OUT_PATH)

    runtime = time.time() - start_time
    print("=" * 55)
    print(f"  Pipeline complete. Total runtime: {runtime:.2f} seconds")
    print("=" * 55)

if __name__ == "__main__":
    run_pipeline()
