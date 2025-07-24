# Find the indices of the N largest values in an array.
import numpy as np
arr=np.array([5,6,1,2,8,9,3])
indice=np.argpartition(arr,-3)[-3:]
indice=indice[np.argsort(-arr[indice])]
print(indice)
