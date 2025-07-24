# Replace the max value in each row with 0.
import numpy as np
arr=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
max=np.max(arr,axis=1,keepdims=True)
x=np.where(arr==max,0,arr)
print(x)
