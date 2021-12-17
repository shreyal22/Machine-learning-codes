import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('ign.csv')
xbox_df=df[(df['score']>7) & (df['platform']=='Xbox One')]
games_list=xbox_df['title']
print(games_list)
xbox_one =  df[df['platform']=="Xbox One"]
xbox_one_reviews = xbox_one['score_phrase']
xbox_one_reviews.hist(bins=20, grid=False, xrot=90)
ps4 = df[df['platform']=="PlayStation 4"]
ps4_reviews = ps4['score_phrase']
ps4_reviews.hist(bins=20, grid=False, xrot=90)


