from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes = load_diabetes()

# Get features
diabetes_X = diabetes.data

# Get labels
diabetes_y = diabetes.target

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes_X, diabetes_y)

rmse_val = []  # to store rmse values for different k

for K in range(1, int(sqrt(len(X_train))),2):
    model = KNeighborsRegressor(n_neighbors=K)

    model.fit(X_train, y_train)  # fit the model
    pred = model.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    rmse_val.append(error)  # store rmse values
    print('RMSE value for k= ', K, 'is:', error)

plt.plot(range(1, int(sqrt(len(X_train))),2),rmse_val)
plt.show()
