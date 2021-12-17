import pandas as pd
import numpy as np
df=pd.read_csv('Salary_Classification.csv')
df.isnull().any(axis=0)
features=df.iloc[:,0:4].values
labels=df.iloc[:,-1].values
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)
features = features[:,1:]
import statsmodels.api as sm
import numpy as np
features = sm.add_constant(features)
features_optimal = features[:, [0,1,2,3,4,5]]
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, p_values.argmax(),1)
    else:
        break
print (features_optimal.shape)


