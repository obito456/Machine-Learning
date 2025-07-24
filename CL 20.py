# Set the diagonal of a square matrix to 1 (without loops).
import numpy as np
arr=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
np.fill_diagonal(arr,1)
print(arr)
