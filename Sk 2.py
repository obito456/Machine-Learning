import numpy as np
from sklearn.model_selection import train_test_split

x=np.array([1,2,3,4,5])
y=np.array([15,30,45,60,75])
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42,shuffle=True)
print(x_train.shape,x_test.shape)
print(y_train.shape,y_test.shape)
