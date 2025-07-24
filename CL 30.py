# Find the unique values and their counts in an array.
import numpy as np
arr=np.array([1,2,3,4,5,1,2,4,8,9])
unique,values=np.unique(arr,return_counts=True)
print(unique)
print(values)
