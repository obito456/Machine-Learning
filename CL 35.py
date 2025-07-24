# Pad a 2D array with zeros to increase its shape (e.g., (3,3) → (5,5)).
import numpy as np
arr=np.array([ [1,2,3],[4,5,6],[7,8,9] ])
x=np.pad(arr,pad_width=1,mode="constant",constant_values=0)
print(x)
