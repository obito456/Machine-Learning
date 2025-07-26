import numpy as np
import matplotlib.pyplot as plt
a=np.random.randint(100,size=(100))
b=np.random.randint(100,size=(100))
color=np.random.randint(100,size=(100))
size=10*np.random.randint(100,size=(100))
plt.scatter(a,b,c=color,s=size,alpha=0.3,cmap='nipy_spectral')
plt.colorbar()
plt.show()
