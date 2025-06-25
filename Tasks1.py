import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_excel('data.xlsx')
print(data.head())
data['Order Date'] = pd.to_datetime(data['Order Date'])
plt.figure(figsize=(12, 6))
plt.plot(data['Order Date'], data['Sales'], label='Sales', color='blue')
plt.plot(data['Order Date'], data['Profit'], label='Profit', color='green')
plt.title("Stacked Line Chart (Order Date vs Sales & Profit)")
plt.xlabel("Order Date")
plt.ylabel("Amount")
plt.legend()
plt.show()