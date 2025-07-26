import numpy as np
import matplotlib.pyplot as plt
x=["Civil","ECE","CSE"]
y=np.array([25,35,40])
ex=[0,0.2,0]
plt.pie(y,labels=x,explode=ex)
plt.show()
