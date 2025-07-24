# Calculate the determinant & inverse of a square matrix.
import numpy as np
arr=np.array([ [1,2],[3,4] ])
x=np.linalg.det(arr)
y=np.linalg.inv(arr)
print(x)
print(y)
