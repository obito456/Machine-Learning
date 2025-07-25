import numpy as np
import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.array([10,50,25,35,45,16,40,60,38,22])
size=np.array([10,20,30,40,50,60,70,180,10,40])
plt.scatter(a,b,s=size)
plt.show()
