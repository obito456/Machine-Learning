# Split an array into 3 equal parts vertically and horizontally.
import numpy as np
arr=np.arange(36).reshape(6,6)
x=np.hsplit(arr,3)
y=np.vsplit(arr,3)
print(arr)
print(x)
print(y)
