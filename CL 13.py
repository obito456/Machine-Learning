# Swap two rows in a 2D array (e.g., swap row 1 and row 2).
import numpy as np
arr=np.array([ [1,2,3],[4,5,6] ])
arr[[0,1]]=arr[[1,0]]
print(arr)
