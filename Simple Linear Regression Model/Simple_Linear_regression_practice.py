#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Import data
datasets=pd.read_csv('Salary_Data.csv')

#Independent and Dependent varibales
X=datasets.iloc[:,:-1].values
Y=datasets.iloc[:,1].values

#Spliting into train and test sets
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

# Linear Regressiong model take cares the scaling features

#Fitting train set into LinearRegression model
from sklearn.linear_model import LinearRegression
lin_obj=LinearRegression()
lin_obj.fit(X_train,Y_train)
Y_pred=lin_obj.predict(X_test)

#visualization
#Plotting graph of train set with linear regression fit line
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,lin_obj.predict(X_train))
plt.title("Experience Vs Salary (Train Set)")
plt.xlabel('Experience')
plt.ylabel("Salary")
plt.show()

#Plotting graph of test_set with linear regression fit line
plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,lin_obj.predict(X_train))
plt.title("Experience Vs Salary (Test Set)")
plt.xlabel('Experience')
plt.ylabel("Salary")
plt.show()


