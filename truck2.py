import pandas as pd
dataset = pd.read_csv("Foodtruck.csv")
features = dataset.iloc[:,0:1].values
labels = dataset.iloc[:,1:2].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

print(regressor.predict([[3.073]]))

print(regressor.predict([[33.4]]))