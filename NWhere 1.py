import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
a=np.where(arr==4)
b=np.where(arr%2==0)
print(a)
print(b)
