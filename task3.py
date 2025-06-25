import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_excel('data.xlsx')
print(data.head())
data['Order Date'] = pd.to_datetime(data['Order Date'])
fig = px.line(data, x='Order Date', y=['Sales', 'Profit', 'Quantity'], title='Stacked Line Chart (Order Date vs Sales, Profit, Quantity)')
fig.show()
