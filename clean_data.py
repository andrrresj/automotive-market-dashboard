import pandas as pd
import numpy as np

print("🧹 CLEANING AUTOMOTIVE DATA...\n")

# ============================================
# CLEAN DATASET 1: Sales Data
# ============================================
print("=" * 60)
print("Cleaning Sales Data (car_prices.csv)")
print("=" * 60)

df_sales = pd.read_csv('car_prices.csv')
print(f"Starting rows: {len(df_sales):,}")

# Remove rows with missing critical data
df_sales = df_sales.dropna(subset=['make', 'sellingprice', 'year'])
print(f"After removing missing make/price/year: {len(df_sales):,}")

# Remove invalid prices (less than $1000 or over $200k for realistic analysis)
df_sales = df_sales[(df_sales['sellingprice'] >= 1000) & (df_sales['sellingprice'] <= 200000)]
print(f"After price filtering: {len(df_sales):,}")

# Remove very old cars (keep 2000+)
df_sales = df_sales[df_sales['year'] >= 2000]
print(f"After year filtering (2000+): {len(df_sales):,}")

# Create luxury brand flag
luxury_brands = ['Mercedes-Benz', 'BMW', 'Audi', 'Lexus', 'Porsche', 
                 'Cadillac', 'Lincoln', 'Infiniti', 'Acura', 'Jaguar',
                 'Land Rover', 'Volvo', 'Tesla']

df_sales['is_luxury'] = df_sales['make'].isin(luxury_brands)

# Create brand categories
def categorize_brand(make):
    if make in ['Mercedes-Benz', 'BMW', 'Audi']:
        return 'German Luxury'
    elif make in ['Lexus', 'Infiniti', 'Acura']:
        return 'Japanese Luxury'
    elif make in ['Cadillac', 'Lincoln', 'Tesla']:
        return 'American Luxury'
    elif make in luxury_brands:
        return 'Other Luxury'
    else:
        return 'Mass Market'

df_sales['brand_category'] = df_sales['make'].apply(categorize_brand)

# Create vehicle age
df_sales['vehicle_age'] = 2024 - df_sales['year']

# Save cleaned sales data
df_sales.to_csv('sales_cleaned.csv', index=False)
print(f"\n✅ Sales data cleaned: {len(df_sales):,} rows saved")

# ============================================
# CLEAN DATASET 2: Specifications
# ============================================
print("\n" + "=" * 60)
print("Cleaning Specifications Data (data.csv)")
print("=" * 60)

df_specs = pd.read_csv('data.csv')
print(f"Starting rows: {len(df_specs):,}")

# Remove rows with missing critical data
df_specs = df_specs.dropna(subset=['Make', 'MSRP', 'Engine HP'])
print(f"After removing missing make/MSRP/HP: {len(df_specs):,}")

# Remove invalid MSRP
df_specs = df_specs[(df_specs['MSRP'] >= 10000) & (df_specs['MSRP'] <= 300000)]
print(f"After MSRP filtering: {len(df_specs):,}")

# Keep recent years
df_specs = df_specs[df_specs['Year'] >= 2000]
print(f"After year filtering (2000+): {len(df_specs):,}")

# Add luxury flag
df_specs['is_luxury'] = df_specs['Make'].isin(luxury_brands)

# Add brand category
df_specs['brand_category'] = df_specs['Make'].apply(categorize_brand)

# Clean Market Category column (handle multiple categories)
df_specs['is_performance'] = df_specs['Market Category'].fillna('').str.contains('Performance|Exotic|High-Performance')
df_specs['is_luxury_cat'] = df_specs['Market Category'].fillna('').str.contains('Luxury')

# Save cleaned specs data
df_specs.to_csv('specs_cleaned.csv', index=False)
print(f"\n✅ Specs data cleaned: {len(df_specs):,} rows saved")

# ============================================
# SUMMARY STATISTICS
# ============================================
print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print("\n📊 Sales Data Summary:")
print(f"Total luxury cars: {df_sales['is_luxury'].sum():,} ({df_sales['is_luxury'].mean()*100:.1f}%)")
print(f"Average selling price: ${df_sales['sellingprice'].mean():,.2f}")
print(f"Average luxury price: ${df_sales[df_sales['is_luxury']]['sellingprice'].mean():,.2f}")

print("\n🏢 Top 10 Brands by Volume:")
print(df_sales['make'].value_counts().head(10))

print("\n🏆 German Luxury Brands:")
german_luxury = df_sales[df_sales['brand_category'] == 'German Luxury']
print(f"Total: {len(german_luxury):,} cars")
print(german_luxury['make'].value_counts())

print("\n🌍 Top 10 States:")
print(df_sales['state'].value_counts().head(10))

print("\n💰 Price Distribution by Category:")
price_by_cat = df_sales.groupby('brand_category')['sellingprice'].agg(['mean', 'median', 'count'])
print(price_by_cat.sort_values('mean', ascending=False))

print("\n" + "=" * 60)
print("🎉 DATA CLEANING COMPLETE!")
print("=" * 60)
print("\nCleaned files created:")
print("  ✅ sales_cleaned.csv")
print("  ✅ specs_cleaned.csv")
