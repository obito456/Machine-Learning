import numpy as np
import matplotlib.pyplot as plt
x=["Civil","ECE","CSE"]
y=np.array([25,35,40])
color=['yellow','red','pink']
plt.pie(y,labels=x,shadow=True,colors=color)
plt.legend(title="Branch")
plt.show()
