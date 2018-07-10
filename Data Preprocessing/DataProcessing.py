
#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import DataSets
datasets=pd.read_csv('Data.csv')
x=datasets.iloc[:,:-1].values
y=datasets.iloc[:,3].values


#Handling missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='most_frequent',axis=0)
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])


#Handling Categorical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encode_x=LabelEncoder()
x[:,0]=label_encode_x.fit_transform(x[:,0])


#But here it converted into 1,2,3 of 3 categories, to over come this uses dummy Encoding
onehotEncoder_x=OneHotEncoder(categorical_features=[0])
x=onehotEncoder_x.fit_transform(x).toarray()
label_encode_y=LabelEncoder()
y=label_encode_y.fit_transform(y)


#Spliting the data in to train and test sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


#Scalling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_x.transform(x_test)



