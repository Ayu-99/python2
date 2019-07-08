from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score

# 1st step -> Prepare your data
#              Train our model-> Supervised Learning
table = pd.read_csv("advertising.csv")

X = table.Radio.values
Y = table.Sales.values
# print(X)
# print()
# print(Y)


X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

# We need 2D array to train our LinearRegression Model from skLearn

# 2nd Step->To create model
model = LinearRegression()  # Object creation statement

# 3rd Step-> Fit Function is to Train Model with data and data should be 2d arrays
#             Also optimize our model
model.fit(X, Y)

# 4th Step: Predictions on original data so as to get predicted Y i.e Y1
Y1 = model.predict(X)
# real X and getting predicted Y

score = r2_score(Y, Y1)
print("R2 score for our model is", score)

b0 = model.intercept_
b1 = model.coef_
print("Intercpter is:", b0)
print("Slope is:", b1)


