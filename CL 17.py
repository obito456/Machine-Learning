# Find indices of non-zero elements in a 1D array.
import numpy as np
arr=np.array([1,2,3,4,0,5,0,7])
a=np.where(arr>0)
b=np.nonzero(arr)
print(a)
print(b)
print(a[0])
print(b[0])
