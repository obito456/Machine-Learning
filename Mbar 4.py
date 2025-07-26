import numpy as np
import matplotlib.pyplot as plt
a=np.array(['A','B','C','D'])
b=np.array([20,30,15,10])
plt.barh(a,b,color='red',height=0.1)
plt.show()
