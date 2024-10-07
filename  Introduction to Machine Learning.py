import numpy as np
from sklearn.linear_model import LinearRegression

# Introduction to Machine Learning with Linear Regression

import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_new = np.array([[0], [2]])
y_predict = model.predict(X_new)

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X_new, y_predict, color='red', linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Example")
plt.show()

# Print the model parameters
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)