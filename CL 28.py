# Solve a system of linear equations (e.g., 2x + 3y = 5, 4x + y = 6).
import numpy as np
a=np.array([ [2,3],[4,1] ])
b=np.array([5,6])
x=np.linalg.solve(a,b)
print(x[0])
print(x[1])


