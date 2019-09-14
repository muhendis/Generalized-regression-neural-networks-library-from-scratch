import numpy as np
import pandas as pd

class GRNN :

    def __init__(self,x_train,y_train,x_test,y_test):

        self.x_train= x_train
        self.y_train= y_train
        self.x_test= x_test
        self.y_test= y_test

        self.std     = np.ones((1,self.y_train.size))#np.random.rand(1,self.train_y.size) #Standard deviations(std) are sometimes called RBF widths.

    def activation_func(self,distances): # gaussian kernel
        
        return np.exp(- (distances**2) / 2*(self.std**2) )

    def output(self,i):#sometimes called weight

        distances=np.sqrt(np.sum((self.x_test[i]-self.x_train)**2,axis=1)) # euclidean distance
        
        return self.activation_func(distances)
   
    def denominator(self,i):

        return np.sum(self.output(i))

    def numerator(self,i): 

        return  np.sum(self.output(i) * self.y_train)
    
    def predict(self):

        predict_array = np.array([])

        for i in range(self.y_test.size):
            predict=np.array([self.numerator(i)/self.denominator(i)])
            predict_array=np.append(predict_array,predict)
        
        return predict_array
    
    def mean_squared_error(self):

        return (self.predict()-self.y_test)**2 /self.y_test.size
    
    def root_mean_squared_error(self):

        return np.sqrt(self.mean_squared_error())
