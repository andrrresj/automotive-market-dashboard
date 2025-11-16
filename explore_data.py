import pandas as pd
import numpy as np

print("🏎️ AUTOMOTIVE MARKET DATA EXPLORATION\n")

# ============================================
# DATASET 1: Vehicle Sales Data
# ============================================
print("=" * 60)
print("DATASET 1: Vehicle Sales Data (car_prices.csv)")
print("=" * 60)

try:
    df_sales = pd.read_csv('car_prices.csv')
    
    print(f"\n📊 Basic Info:")
    print(f"Total records: {len(df_sales):,}")
    print(f"Columns: {len(df_sales.columns)}")
    
    print(f"\n📋 Column names:")
    print(df_sales.columns.tolist())
    
    print(f"\n👀 First 5 rows:")
    print(df_sales.head())
    
    print(f"\n📈 Data types:")
    print(df_sales.dtypes)
    
    print(f"\n❓ Missing values:")
    missing = df_sales.isnull().sum()
    print(missing[missing > 0])
    
    # Check for brand/make column
    brand_cols = [col for col in df_sales.columns if 'make' in col.lower() or 'brand' in col.lower()]
    if brand_cols:
        brand_col = brand_cols[0]
        print(f"\n🏢 Brand column found: '{brand_col}'")
        print(f"Unique brands: {df_sales[brand_col].nunique()}")
        print("\nTop 15 brands by count:")
        print(df_sales[brand_col].value_counts().head(15))
    
    print("\n✅ Dataset 1 loaded successfully!")
    
except FileNotFoundError:
    print("❌ Error: car_prices.csv not found in folder")
except Exception as e:
    print(f"❌ Error loading dataset 1: {e}")

print("\n" + "=" * 60)

# ============================================
# DATASET 2: Car Specifications
# ============================================
print("DATASET 2: Car Specifications (data.csv)")
print("=" * 60)

try:
    df_specs = pd.read_csv('data.csv')
    
    print(f"\n📊 Basic Info:")
    print(f"Total records: {len(df_specs):,}")
    print(f"Columns: {len(df_specs.columns)}")
    
    print(f"\n📋 Column names:")
    print(df_specs.columns.tolist())
    
    print(f"\n👀 First 5 rows:")
    print(df_specs.head())
    
    print(f"\n📈 Data types:")
    print(df_specs.dtypes)
    
    # Check for luxury brands
    if 'Make' in df_specs.columns:
        print(f"\n🏢 Unique makes: {df_specs['Make'].nunique()}")
        print("\nTop 15 makes:")
        print(df_specs['Make'].value_counts().head(15))
    
    print("\n✅ Dataset 2 loaded successfully!")
    
except FileNotFoundError:
    print("❌ Error: data.csv not found in folder")
except Exception as e:
    print(f"❌ Error loading dataset 2: {e}")

print("\n" + "=" * 60)
print("🎉 Exploration Complete!")
print("=" * 60)

