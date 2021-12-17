import numpy as np
from numpy.lib.shape_base import array_split
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import series
df=pd.read_csv('titanic.csv')
survived=df['Survived'].value_counts()[1]
print(str(survived)+' people survived!!')
per=((survived/len(df['Survived']))*100)
print(str(per)+'% people survived.')
died=df['Survived'].value_counts()[0]
print(str(died)+' people died :(')
died_per=((died/len(df['Survived']))*100)
print(str(died_per)+'% people died ')
man_survived=df['Survived'][df['Sex']=='male'].value_counts(normalize=True)[1]
print(str(round(float(man_survived)*100,2))+"% male survived")


man_died=df['Survived'][df['Sex']=='male'].value_counts(normalize=True)[0]
print(str(round(float(man_died)*100,2))+"% male died")

f_survived=df['Survived'][df['Sex']=='female'].value_counts(normalize=True)[1]
f_died=df['Survived'][df['Sex']=='female'].value_counts(normalize=True)[0]
print(str(round(float(f_survived)*100,2))+"% female survived")
print(str(round(float(f_died)*100,2))+"% female died")

child_survived=df['Survived'][df['Age']<=18].value_counts(normalize=True)[1]
print(str(round(float(child_survived)*100,2))+"% children survived")
