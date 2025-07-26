import numpy as np
import matplotlib.pyplot as plt
x=["Civil","ECE","CSE"]
y=np.array([25,35,40])
plt.pie(y,labels=x,startangle=90)
plt.show()
