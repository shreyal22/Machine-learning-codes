
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('Foodtruck.csv')
labels=df.iloc[:,0:1].values
features=df.iloc[:,1:2].values

features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

regressor=LinearRegression()
regressor.fit(features_train,labels_train)
print(regressor.predict([[3.073]]))
print(regressor.predict([[33.4]]))


