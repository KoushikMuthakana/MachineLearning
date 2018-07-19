#Importing Libraries
from numpy import *
from pandas import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

#Importing Data
datasets=read_csv('student.csv')
x1=datasets.iloc[:,0].values
x2=datasets.iloc[:,1].values
y=datasets.iloc[:,2].values

#Plotting 3D graph
fig=figure()
ax=Axes3D(fig)
ax.scatter(x1,x2,y,color='red')
show()

# Creating Independents
x0=ones(len(x1))
X=array([x0,x1,x2]).T

#Creating Initial Coefficients
B=array([0,0,0])


def cost_function(X,B,y):

    cost=(((X.dot(B)-y)**2).sum())/(2*len(y))
    return cost

def gradiant_decent(alpha,B,X,y,iteration_count):
    '''
    m1= m1-alpha*(1/m)* error *x1
    '''

    for i in range(iteration_count):
      loss=(X.dot(B)-y)
      gradient=X.T.dot(loss) /len(y)
      B=B-alpha*gradient
      cost=cost_function(X,B,y)
    return cost,B


def Root_Mean_Squared_Error(y_pred,y):

    rmse=sqrt(sum((y_pred-y)**2/len(y)))
    return rmse

def r2_Score(y,y_pred):
    mean_y=mean(y)
    sst=sum((y-mean_y)**2)
    ssr=sum((y-y_pred)**2)
    r2=1-(ssr/sst)
    return r2

print("Initial Coefficients : ",B)
print("Initial Cost         : ",cost_function(X,B,y))

alpha=0.0001
iteration_count=100000
cost,new_B=gradiant_decent(alpha,B,X,y,iteration_count)

print("New Coefficients : ",new_B)
print("Minimized Cost   : ",cost)

Y_pred=X.dot(new_B)

#Calculating Model score
rmse=Root_Mean_Squared_Error(Y_pred,y)

#Calculation R2 Score
r2=r2_Score(y,Y_pred)

print("RMSE Score : ",rmse)
print("R2 Score   :",r2)

#Using Scikit_Learn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
regressor=LinearRegression()
regressor.fit(X,y)
y_pred1=regressor.predict(X)
print("R2 Score Using SciKit_learn  :",regressor.score(X,y))
print("RMSE using SciKit_learn      : ", sqrt(mean_squared_error(y,y_pred1)))
fig1=figure()
dx1=Axes3D(fig1)
dx1.scatter(x1,x2,Y_pred)
show()














