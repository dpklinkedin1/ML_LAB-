import numpy as np
from sklearn.linear_model import LogisticRegression

# Input (hours studied)
X = np.array([[1], [2], [3], [4], [5]])

# Output (0 = Fail, 1 = Pass)
y = np.array([0, 0, 0, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# New input
new_value = np.array([[3]])

# Predict class
prediction = model.predict(new_value)

# Predict probability
prob = model.predict_proba(new_value)

# Output
print("Prediction (0=Fail, 1=Pass) =", prediction[0])
print("Probability =", prob[0])
