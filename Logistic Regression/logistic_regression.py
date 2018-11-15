from sklearn import datasets
import numpy as np

iris=datasets.load_iris()
X=iris.data[:,:2]
Y=(iris.target!=0)*1
class LogisticRegression(object):
    def __init__(self,lr=0.01,itr_count=10000):
        self.lr=lr
        self.itr_count=itr_count
        self._intercept=None
        self._coef=None
        
    def addIntercept(self,X):
        ones=np.ones((X.shape[0],1))
        return np.concatenate((ones,X),axis=1)
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
    
    def lossFunction(self,h,Y):
        return ((-Y.T*np.log(h))-((1-Y).T*np.log(1-h))).mean()       
    
    def gradient(self,X,Y,h):
        return np.dot( X.T, (h-Y))/X.shape[0]

    def fit( self,X,Y):
        X=self.addIntercept(X)
        self.theta=np.zeros(X.shape[1])
        for i in range(self.itr_count):
            z=np.dot(X,self.theta)
            h=self.sigmoid(z)
            grad=self.gradient(X,Y,h)
            self.theta-=self.lr*grad
        
        z=np.dot(X,self.theta)
        h=self.sigmoid(z)
        loss=self.lossFunction(h,Y)
        self._intercept=self.theta[0]
        self._coef=self.theta[1:]
        print('Loss : {0}'.format(loss))
    
    def predict(self,X,threshold=0.5):
        X=self.addIntercept(X)
        res= [ 1 if i >=threshold else 0 for i in self.sigmoid(np.dot(X,self.theta))]
        return np.array(res)
               
                
reg=LogisticRegression()
reg.fit(X,Y)
pred_y=reg.predict(X)
print(reg._intercept,reg._coef)


'''
Using Sklear Logistic Regression

'''
from sklearn.linear_model import LogisticRegression
reg=LogisticRegression()
reg.fit(X,Y)
y_pred=reg.predict(X)

print(reg.intercept_,reg.coef_)