import numpy as np
arr=np.array([1,2,3])
arr1=arr.copy()
arr2=arr.view()
print(arr1.base)
print(arr2.base)
