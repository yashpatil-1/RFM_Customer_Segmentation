import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "online_retail_II.xlsx"

print("Loading dataset...")

xls = pd.ExcelFile(DATA_FILE)

print("\nSheets available:")
print(xls.sheet_names)

for sheet in xls.sheet_names:
    df = pd.read_excel(DATA_FILE, sheet_name=sheet)

    print("\n" + "=" * 60)
    print(f"SHEET: {sheet}")
    print("=" * 60)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nBasic statistics:")
    print(df.describe(include="all").transpose())