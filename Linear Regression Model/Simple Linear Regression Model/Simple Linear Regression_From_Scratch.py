import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Using Least Square Error Method:
    Simple Linear Equation : Y=β0+β1X
      Coefficient : β1=   ∑ (xi−x¯)(yi−y¯)
                          mi=1
                        -----------------------
                          ∑ (xi−x¯)**2
                          mi=1
                          
                        y¯=Mean of  Y
                        x¯=Mean of  X
          
       Bias Coefficient (Constant): β0= y¯−β1x¯ 
    
'''
plt.rcParams['figure.figsize']=(10.0,5.0)
datasets=pd.read_csv('headbrain.csv')
print(datasets.shape)
print(datasets.head())

x=datasets['Head Size(cm^3)'].values
y=datasets['Brain Weight(grams)'].values

#Mean values
x_mean=np.mean(x)
y_mean=np.mean(y)

x_len=len(x)
num=0
den=0

# coefficients b0 and b1
for i in range(x_len):
    num+=(x[i]-x_mean)*(y[i]-y_mean)
    den+=(x[i]-x_mean)**2
b1=num/den
b0=(y_mean)-(b1*x_mean)
print(b0,b1)

# X-axis range
max_x = np.max(x) + 100
min_x = np.min(x) - 100


#Cordinates X and Y
model_x = np.linspace(min_x, max_x, 1000)
model_y=b0+b1*model_x


#Plotting model Line
plt.plot(model_x,model_y, color='blue')
plt.title("Simple Linear Model")
plt.xlabel('Head Size')
plt.ylabel('Brain Weight')


#Scattering the dataset
plt.scatter(x,y,color='red')
plt.show()


'''
methods to evaluate models.                      m
      Root Mean Squared Error            :squrt( ∑ yi^−yi)**2/m )
                                                 i=1
     
     
     Coefficient of Determination(R2 Score):
                m 
            SSt=∑(yi−y¯)**2
                i=1
                m 
            SSt=∑(yi−yi^)**2
                i=1
            R2= 1− (SSr/SSt)
'''

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
x=np.reshape(x,(len(x),1))
reg.fit(x,y)
y_pred=reg.predict(x)
print(reg.score(x,y))

















