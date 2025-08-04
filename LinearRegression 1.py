import numpy as np
from sklearn.linear_model import LinearRegression

house = np.array([50, 60, 70, 80, 90]).reshape(-1, 1) 
price = np.array([150, 180, 210, 240, 270])  
model=LinearRegression().fit(house,price)
print(model.predict([[83]]))
