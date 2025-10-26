import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
data_path = os.path.join('..', 'data', 'products.csv')
df = pd.read_csv(data_path)

# Clean and prepare data
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df = df.dropna(subset=['Category', 'Availability', 'Price'])

# Group by Category and Availability
grouped = df.groupby(['Category', 'Availability']).agg({'Price': 'mean'})
grouped['Count'] = df.groupby(['Category', 'Availability']).size().values
grouped = grouped.reset_index()

# Define color palette
palette = {
    'in_stock': '#4CAF50',
    'pre_order': '#FF9800',
    'out_of_stock': '#F44336'
}

# Create the plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=grouped,
    x='Category',
    y='Price',
    size='Count',
    hue='Availability',
    palette=palette,
    sizes=(200, 800),
    alpha=0.8,
    edgecolor='black'
)

# Style the plot
plt.title('📦 Average Price by Category Based on Availability', fontsize=14)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Average Price (USD)', fontsize=12)
plt.xticks(rotation=30, ha='right')
plt.legend(title='Availability Status', loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the plot
output_path = os.path.join('..', 'images', 'category_price_availability.png')
plt.savefig(output_path)
print(f"✅ Visualization saved to {output_path}")
