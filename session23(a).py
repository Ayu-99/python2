import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
data = pd.read_csv('advertising.csv')

l1 = data.TV.tolist()
print(l1)

l2 = data.Sales.tolist()
print(l2)

data = stats.linregress(l1, l2)
maxX = max(l1) + 10
minX = min(l1) - 10
x = np.linspace(maxX, minX, 100)
y = data[1] + data[0]*x

plt.xlabel("Advertising through Tv")
plt.ylabel("No. of Sales")
plt.grid("True")
plt.plot(x, y, color="r", label="Regression Line")
plt.plot(l1, l2, "o", color="b", label="Data Points")
plt.legend()
plt.show()


