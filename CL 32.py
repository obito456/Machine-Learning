# Reshape a 1D array into a 3D array (e.g., shape (2,3,4)).
import numpy as np
arr=np.arange(24)
x=arr.reshape(2,3,4)
print(x)
print(x.ndim)
