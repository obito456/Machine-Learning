# Replace the max value in each row with 0.
import numpy as np
arr1=np.array([ [1,2,3],[6,5,4],[7,8,9] ])
arr2=np.array([ [7,8,9],[1,2,3],[6,5,4] ])
x=np.sort(arr1,axis=1)
y=np.sort(arr2,axis=0)
print(x)
print(y)
