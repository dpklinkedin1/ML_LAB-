import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Dataset
data = {
    "Area": [1000,1500,2000,2500,3000],
    "Bedrooms": [2,3,3,4,4],
    "Age": [10,5,8,3,1],
    "Price": [200000,300000,350000,400000,500000]
}

df = pd.DataFrame(data)

# Features & Target
X = df[["Area","Bedrooms","Age"]]
y = df["Price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = DecisionTreeRegressor()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
