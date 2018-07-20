import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datasets=pd.read_csv('Position_Salaries.csv')
print(datasets.head())

x=datasets['Level'].values
y=datasets['Salary'].values
x=np.reshape(x,(len(x),1))


#Plotting with original dataset
plt.scatter(x,y,color='red')
plt.title('Position Vs Salaries (Original Data)')
plt.xlabel('Position')
plt.ylabel("Salaries")
plt.show()

#Fitting LinearRegression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Position Vs Salaries (Linear Regression Model)')
plt.xlabel('Position')
plt.ylabel("Salaries")
plt.show()


#Fitting polynomial model to the dataset with degree 2
from sklearn.preprocessing import PolynomialFeatures
poly_obj=PolynomialFeatures(degree=2)
x_poly=poly_obj.fit_transform(x)
lin_reg_2=LinearRegression()
lin_reg_2.fit(x_poly,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(x_poly),color='blue')
plt.title('Position Vs Salaries (Polynomial Regression Model with degree 2)')
plt.xlabel('Position')
plt.ylabel("Salaries")
plt.show()


 #Plotting the polynomial Model with degree 3
poly_obj=PolynomialFeatures(degree=3)
poly_x_3=poly_obj.fit_transform(x)
lin_reg_3=LinearRegression()
lin_reg_3.fit(poly_x_3,y)
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_3.predict(poly_x_3),color='blue')
plt.title('Position Vs Salaries (Polynomial Regression Model with degree 3)')
plt.xlabel('Position')
plt.ylabel("Salaries")
plt.show()


#Plotting the polynomial Model with degree 4
x_grid=np.arange(min(x),max(x),0.1)
x_grid=np.reshape(x_grid,(len(x_grid),1))
poly_obj_4=PolynomialFeatures(degree=4)
poly_x_4=poly_obj_4.fit_transform(x)
lin_4=LinearRegression()
lin_4.fit(poly_x_4,y)
plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_4.predict(poly_obj_4.fit_transform(x_grid)))
plt.title('Position Vs Salaries (Polynomial Regression Model with degree 4)')
plt.xlabel('Position')
plt.ylabel("Salaries")
plt.show()

#Predicting the Salary Linear Regression Vs Polynomial Regression
y_pred= lin_reg.predict(3)
print("Prediction Using Linear Regression",y_pred)
Y_pred=lin_4.predict(poly_obj_4.fit_transform(3))
print("Prediction Using polynomial Regression",Y_pred)















