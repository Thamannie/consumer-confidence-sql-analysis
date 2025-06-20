import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
file_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\data\exports\extreme_monthly_changes.csv'
df = pd.read_csv(file_path)

# Format month
df['month'] = pd.to_datetime(df['month'])
df['month_str'] = df['month'].dt.strftime('%Y-%m')

# Ensure order
df['type'] = pd.Categorical(df['type'], categories=['Max Loss', 'Max Gain'], ordered=True)
df = df.sort_values(['ticker', 'type']).reset_index(drop=True)

# Plot
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=df,
    x='ticker',
    y='pct_change',
    hue='type',
    palette={'Max Gain': 'seagreen', 'Max Loss': 'crimson'}
)

# Add month labels to each bar
for bars, (_, sub_df) in zip(ax.containers, df.groupby('type')):
    for bar, label in zip(bars, sub_df['month_str']):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (2 if height > 0 else -4),
            label,
            ha='center',
            va='bottom' if height > 0 else 'top',
            fontsize=8
        )

# Final touches
plt.title('Extreme Monthly % Changes by Brand (2020–2024)\nLabeled with Month')
plt.xlabel('Brand')
plt.ylabel('Monthly % Change')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
plt.legend(title='Type of Change')
plt.tight_layout()

# Save
output_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\output\visuals\extreme_monthly_changes.png'
plt.savefig(output_path)
plt.show()
