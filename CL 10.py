# Generate a 10×10 array where each element is the sum of its row and column indices.
import numpy as np
arr=np.fromfunction(lambda i,j:i+j ,(10,10),dtype="i")
print(arr)
