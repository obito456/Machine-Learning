# Broadcast a 1D array to add to each row of a 2D array.
import numpy as np
arr1=np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ])
arr2=np.array([10,20,30,40])
arr=arr1+arr2
print(arr)
