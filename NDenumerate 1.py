import numpy as np
arr=np.array([ [1,2,3],[4,5,6] ])
for x,y in np.ndenumerate(arr):
    print(x,y)
