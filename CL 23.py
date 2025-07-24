# Normalize a 2D array (subtract mean, divide by std).
import numpy as np
arr=np.array([ [1,2,3],[4,5,6],[7,8,9] ],dtype="float")
meanx=np.mean(arr,axis=0)
stdx=np.std(arr,axis=0)
x=(arr-meanx)/stdx
print(x)
