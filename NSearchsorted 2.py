import numpy as np
arr=np.array([1,2,3,4,5,6,7])
a=np.searchsorted(arr,6,side='right')
print(a)
