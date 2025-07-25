import numpy as np
import matplotlib.pyplot as plt
a=np.array([1,2,3])
b=np.array([140,240,420])
c=np.array([10,20,30])
d=np.array([5,7,20])
plt.subplot(2,1,2)
plt.plot(a,b)
plt.subplot(2,1,1)
plt.plot(c,d)
plt.suptitle("Home")
plt.show()
