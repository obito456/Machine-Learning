# Generate a checkerboard pattern (alternating 0s and 1s) of size 8×8.
import numpy as np
arr=np.ones((8,8),dtype="i")
arr[1::2,::2]=0
arr[::2, 1::2]=0
print(arr)
