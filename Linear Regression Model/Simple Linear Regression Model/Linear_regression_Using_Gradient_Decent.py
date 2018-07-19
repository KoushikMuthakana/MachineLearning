
from numpy import *
import matplotlib.pyplot as plt

def compute_error_value(b,m,data):
    error_value=0
    for i in range(len(data)):
        x=data[i,0]
        y=data[i,1]
        error_value+= (y-(m*x+b))**2
    return error_value/float(len(data))

def step_gradiant(b_current,m_current,data,learning_rate):
    # step gradiant
    m_gradiant=0
    b_gradiant=0
    N=float(len(data))
    for i in range(len(data)):
        x=data[i,0]
        y=data[i,1]
        m_gradiant += -(2 / N) * x * (y - ((m_current * x) + b_current))
        b_gradiant += -(2 / N) * (y - ((m_current * x) + b_current))
    new_b=b_current-(learning_rate*b_gradiant)
    new_m=m_current-(learning_rate*m_gradiant)
    return [new_b,new_m]

def gradian_decent(data,starting_b,starting_m,learning_rate,num_iterations):
    b=starting_b
    m=starting_m
    for i in range(num_iterations):
        b,m=step_gradiant(b,m,array(data),learning_rate)
    return [b,m]

def run():
    data=genfromtxt('data.csv',delimiter=',')
    learning_rate=0.0001
    #y=mx+b
    initial_m=0
    initial_b=0
    num_iteration=1000
    [b,m]=gradian_decent(data,initial_b,initial_m,learning_rate,num_iteration)
    x=reshape(data[:,0],(len(data),1))
    y=data[:,1]
    x_model=data[:,0]
    y_model=(m*x_model)+b
    plt.scatter(x_model, y, color='red')
    plt.plot(x_model,y_model)
    plt.title("Linear Regression Using Gradiant_Decent")
    plt.show()

    '''
    Using Scikit-learn
    '''
    from sklearn.linear_model import LinearRegression
    reg=LinearRegression()
    reg.fit(x,y)
    plt.scatter(x, y,color='red')
    plt.title("Linear Regression Using Scikit-learn")
    plt.plot(x,reg.predict(x))
    plt.show()
    from sklearn.metrics import mean_squared_error
    rmse = sqrt(mean_squared_error(y, reg.predict(x)))
    print('Using Sklearn Error :',rmse)
    print('Using Gradiant Error :', sqrt(compute_error_value(b,m,data)))

if __name__=='__main__':
    run()