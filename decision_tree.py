import numpy as np
from sklearn.tree import DecisionTreeRegressor

X = np.array([
    [1000,2,10],
    [1500,3,5],
    [1800,4,2],
    [1200,2,8],
    [2000,5,1]
])

y = np.array([200000,300000,400000,250000,500000])
model = DecisionTreeRegressor()
model.fit(X, y)
new_house = np.array([[1600,3,4]])
price = model.predict(new_house)

print("Predicted Price =", price[0])
