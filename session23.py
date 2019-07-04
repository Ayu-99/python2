"""
    Linear Regression:

    Data: is known to us before hand
    Hence, Supervised Learning
    X = [1, 2, 3, 4, 5]
    Y = [2, 4, 5, 4, 5]

    Equation of Regression Line->
    Y = b0 + b1X

    Primary Objective is to find slope of the line i.e b1 !!

    Step1:
    MX ->3
    MY ->4
    -------------------------------------------------------
    X  Y    X-MX   Y-MY     Sq(X-MX)    (X-MX)(Y-MY)
    --------------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2
    ---------------------------------------------------------

    Step2:
    -------------------------
    Sum of Sq(X-MX) : 10
    Sum of (X-MX)(Y-MY) : 6

    b1 = Slope of line
    b1 = [Sum of (X-MX)(Y-MY) ]/[Sum of Sq(X-MX)]
    b1 = 6/10
    b1 = 0.6


    Step3:

    Equation of Line:
    =================
    Y = b0 + (0.6)X

    Put the mean values of X and Y in equation to find b0
    4 = b0 + (0.6)*3
    4 = b0 + 1.8
    b0 = 2.2

    ========================
    Final Equation of Line:
    ========================
    Y = 2.2 + (0.6)X
    ========================


    Step4:

    Calculate Errors !! Check for the errors if they are more or less !!
    If errors are less then we are good to go else we have to optimize our data

    1.Mean Square Error
    2.R2
    3.Variance

    Lets find MSE
    Substitute original values of X and compute Y in equation of Line
    Y' will be predicted output on basis of equation of Line
    -----------------------------------------------------------
    X  Y    Y'    Y-MY     Sq(Y-MY)   Sq(Y'-MY)
    --------------------------------------------------------
    1   2   2.8     -2        4          1.44
    2   4   3.4      0         0          0.36
    3   5    4       1         1          0
    4   4   4.6      0         0          0.36
    5   5   5.2      1         1          1.44
    ---------------------------------------------------------

    MSE = [Sum of Sq(Y'-MY)]/[Sum of Sq(Y-MY)]
    MSE = 3.6/6
    MSE = 0.6

    if MSE is 0 it means Regression Line is Perfect
    MSE should be nearly 0 so as our prediction goes better

"""

import matplotlib.pyplot as plt
#import numpy as np

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]
print()
sumX = sum(X) / len(X)
sumY = sum(Y) / len(Y)
#print(sumX)

l1 = []
for i in range(len(X)):
    y = (X[i] - sumX)
    l1.append(y*y)

# Sq(X-MX)
sumA = sum(l1)

l2 = []
for i in range(len(Y)):
    y = (Y[i] - sumY)*(X[i] - sumX)
    l2.append(y)

# Sq(Y-MY)
sumB = sum(l2)
#print(sumB)
b1 = sumB/sumA
print("Slope is:", b1)

#print(sumA)

b0 = sumY - 0.6*sumX
print("Intercept is:", b0)

l3 = []
for i in range(len(X)):
    y = 0.6 * X[i] + 2.2
    z = y-sumY
    l3.append(z*z)

#print(sum(l3))
error = sum(l3)/sumB
if error <= 1:
    print("Your Prediction is correct!!")
else:
    print("Your Prediction is Not correct!!")

plt.plot(X, Y, "o")
plt.show()
