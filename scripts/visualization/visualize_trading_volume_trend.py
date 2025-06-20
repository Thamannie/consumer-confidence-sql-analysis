import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
csv_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\data\exports\trading_volume_trend.csv'
df = pd.read_csv(csv_path)

# Convert 'month' column to datetime
df['month'] = pd.to_datetime(df['month'])

# Set style
sns.set(style='whitegrid')

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='month', y='total_monthly_volume', hue='ticker', marker='o')

# Customize the plot
plt.title('Trading Volume Trend Over Time', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Monthly Volume', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
output_path = r'C:\Users\USER\Desktop\consumer-confidence-sql\output\visuals\trading_volume_trend.png'
plt.savefig(output_path)

# Optional: Show the plot
plt.show()

