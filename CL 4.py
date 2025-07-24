# Create a 2D array of shape (4,4) with 1 on the border and 0 inside.
import numpy as np
arr=np.ones((4,4),dtype="i")
arr[1:-1,1:-1]=0
print(arr)
