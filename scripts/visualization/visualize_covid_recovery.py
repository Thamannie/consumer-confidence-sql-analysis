import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\data\exports\covid_pct_changes.csv'
df = pd.read_csv(file_path)

# Convert month to datetime for proper sorting
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# Group by ticker and month to get average pct change
monthly_avg = df.groupby(['ticker', 'month'])['pct_change'].mean().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_avg, x='month', y='pct_change', hue='ticker', marker='o')

plt.title('Brand Performance During COVID-19 Shock (Mar–Jun 2020)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Average Monthly % Change')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save to outputs folder
output_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\output\visuals\covid_recovery_trend.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.close()

print(f"✅ Graph saved to: {output_path}")
plt.show()