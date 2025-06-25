import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_excel('data.xlsx')
print(data.head())
data['Order Date'] = pd.to_datetime(data['Order Date'])
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='Order Date', y='Sales', data=data, ax=ax, label='Sales', color='blue')
ax2 = ax.twinx()
sns.barplot(x='Order Date', y='Profit', data=data, ax=ax2, color='green', alpha=0.5)
ax.set_title("Line Chart with Bar Chart (Order Date vs Sales & Profit)")
ax.set_xlabel("Order Date")
ax.set_ylabel("Sales")
ax2.set_ylabel("Profit")
plt.legend()
plt.show()
fig = px.line(data, x='Order Date', y=['Sales', 'Profit', 'Quantity'], title='Stacked Line Chart (Order Date vs Sales, Profit, Quantity)')
fig.show()
