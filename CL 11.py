#Extract all odd numbers from a given 1D array.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr%2==1)
print(arr[x])
