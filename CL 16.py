# Select rows where the 3rd column value is > 5 in a 2D array.
import numpy as np
arr=np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ])
new=arr[arr[:,2]>5]
print(new)
