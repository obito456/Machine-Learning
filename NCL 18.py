# Replace all NaN values in an array with 0
import numpy as np
arr=np.array([1,2,np.NaN,4,5,5,np.NaN,7])
x=np.nan_to_num(arr,nan=0)
x=x.astype("i")
print(x)
