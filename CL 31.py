# Flatten a 2D array (using ravel() vs flatten()).
import numpy as np
arr=np.array([ [1,2,3],[4,5,6] ])
rav=arr.ravel()
flat=arr.flatten()
print(rav)
print(flat)
