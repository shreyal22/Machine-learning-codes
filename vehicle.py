import numpy as np
from numpy.lib.shape_base import array_split
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import series
df=pd.read_csv('Automobile.csv')
df['price']=df['price'].astype(float)
df['price'].isnull()
df['price']=df['price'].fillna(df['price'].mean())
np_array=df['price'].values
print(df['price'].max())
print(df['price'].min())
print(df['price'].std())
print(df['price'].mean())
Series=df['make'].value_counts()
top_car_makers=Series.index[0:]
vehicle_count=Series.values[0:]
plt.pie(vehicle_count,labels=top_car_makers,autopct='%.2f%%')
plt.show()