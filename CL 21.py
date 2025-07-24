# Multiply two matrices (without np.dot() or @).
import numpy as np
a=np.array([ [1,2],[3,4] ])
b=np.array([ [5,6],[7,8] ])
pro=np.einsum('ik,kj->ij',a,b)
print(pro)
