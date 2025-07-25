import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3])
y=np.array([140,240,420])
font1={'family':'Ariel','color':'red','size':20}
font2={'family':'serif','color':'blue','size':10}
plt.plot(x,y)
plt.xlabel("Quantity",font2)
plt.ylabel("price",font2)
plt.title("Restaurant",font1,loc='right')
plt.show()
