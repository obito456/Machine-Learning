# Compute the Euclidean distance between two vectors.
import numpy as np
a=np.array([1,2,3])
b=np.array([4,0,3])
dist1=np.sqrt(np.sum((a-b)**2))
dist2=np.linalg.norm(a-b)
print(dist1)
print(dist2)
