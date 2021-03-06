#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:41:02 2020

@author: fahadtariq
"""



#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataSet

dataset = pd.read_csv('50_Startups.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy Variable
X = X[:, 1:]


#Splitting Training and Test Set

from sklearn.model_selection import train_test_split

X_train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size = 0.2,random_state = 0 )

#feature Scaling

"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train= sc_X.fit_transform(X_train)
X_Test = sc_X.transform(X_Test)""""

#Multiple Linear Regression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_Train)
y_pred = regressor.predict(X_Test)

#Building the optimal model using backwardelimination

import statsmodels.formula.api as sm

X= np.append(arr = np.ones((50,1)).astype(int) , values = X, axis = 1)

X_opt = X[:, [0,1,2,3,4,5]]

regressor_OLS = sm.OLS(endog = Y,exog = X_opt).fit()

regressor_OLS.summary()

X_opt = X[:, [0,1,3,4,5]]

regressor_OLS = sm.OLS(endog = Y,exog = X_opt).fit()

regressor_OLS.summary()

X_opt = X[:, [0,3,4,5]]

regressor_OLS = sm.OLS(endog = Y,exog = X_opt).fit()

regressor_OLS.summary()

X_opt = X[:, [0,3,5]]

regressor_OLS = sm.OLS(endog = Y,exog = X_opt).fit()

regressor_OLS.summary()

X_opt = X[:, [0,3]]

regressor_OLS = sm.OLS(endog = Y,exog = X_opt).fit()

regressor_OLS.summary()

#Automatic Backward Emimanation

import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)

