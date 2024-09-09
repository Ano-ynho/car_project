# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JQgtxI2V6x24FA8Fx7I6s7LqbKr5Mk9R
"""

import pandas as pd
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt
import seaborn as sns
uploaded=files.upload()
df=pd.read_csv('cars_info.csv')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
print(df.isnull().sum())
df = df[df['Price'] > 0]
df['Model'] = df['Model'].str.strip()
df = df.drop_duplicates()
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Year')
plt.title(' Years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
total_sales = df.groupby('Year')['Price'].sum().reset_index()
top_five_y = total_sales.nlargest(5, 'Price')
top_five= df[df['Year'].isin(top_five_y['Year'])]
print(top_five['Year'])
latest_year=df['Year'].max()
latest_year_data = df[df['Year'] == latest_year]
print(latest_year_data)
brand_count = latest_year_data['Brand'].value_counts()
print(brand_count)
brand_count.to_csv('brand_count.csv', header=True)
files.download('brand_count.csv')