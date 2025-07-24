import numpy as np
arr=np.array([1,2,3])
arr1=arr.view()
arr[0]=5
print(arr1)
