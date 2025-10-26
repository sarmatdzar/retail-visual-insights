import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv('../data/products.csv')

# Convert price to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Remove rows with missing values
df = df.dropna(subset=['Category', 'Availability', 'Price'])

# Grouping
grouped = df.groupby(['Category', 'Availability']).agg({'Price': 'mean'})
grouped['Count'] = df.groupby(['Category', 'Availability']).size().values
grouped = grouped.reset_index()

# Apply a modern style
sns.set_theme(style="whitegrid")

# Color palette
palette = sns.color_palette('pastel', n_colors=len(grouped['Availability'].unique()))

# Visualization
plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    data=grouped,
    x='Category',
    y='Price',
    size='Count',
    hue='Availability',
    palette=palette,
    sizes=(300, 1200),
    alpha=0.85,
    edgecolor='black',
    linewidth=0.7
)

# Add data labels for clarity
for i in range(grouped.shape[0]):
    plt.text(
        x=grouped['Category'][i],
        y=grouped['Price'][i] + 1,  # offset a bit above the point
        s=f"${grouped['Price'][i]:.0f}",
        ha='center',
        fontsize=9,
        color='dimgray'
    )

# Titles and labels
plt.title('Average Product Price by Category and Stock Availability', fontsize=16, weight='bold')
plt.xlabel('Product Category', fontsize=13)
plt.ylabel('Average Price (USD)', fontsize=13)
plt.xticks(rotation=30, ha='right', fontsize=11)
plt.yticks(fontsize=11)

# Legend styling
plt.legend(
    title='Stock Availability',
    title_fontsize=12,
    fontsize=11,
    loc='upper right',
    frameon=True,
    shadow=True
)

# Grid and layout
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
