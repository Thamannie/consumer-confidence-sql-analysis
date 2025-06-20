


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load CSV
df = pd.read_csv('C:/Users/USER/Desktop/consumer-confidence-sql/data/exports/monthly_pct_change.csv')

# Convert month to datetime
df['month'] = pd.to_datetime(df['month'])

# Create the output folder if it doesn't exist
os.makedirs('C:/Users/USER/Desktop/consumer-confidence-sql/output/visuals', exist_ok=True)

# Set style
sns.set(style='whitegrid')

# Create FacetGrid (one line chart per brand)
g = sns.FacetGrid(df, col='ticker', col_wrap=3, height=4, sharey=False)
g.map_dataframe(sns.lineplot, x='month', y='monthly_pct_change', marker='o')
g.set_titles(col_template="{col_name}")
g.set_axis_labels("Month", "Monthly % Change")
for ax in g.axes.flatten():
    ax.tick_params(labelbottom=True)
    ax.tick_params(axis='x', rotation=45)

# Save and show
plt.tight_layout()
g.savefig('C:/Users/USER/Desktop/consumer-confidence-sql/output/visuals/monthly_pct_change_by_brand.png')
plt.show()
