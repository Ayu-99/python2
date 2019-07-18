import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pandas as pd

table = pd.read_csv("faces/face_landmarks.csv")
print(table)

n = 7

imageName = table.iloc[n, 0]
print("Image name is:", imageName)

landMarks =  table.iloc[n, 1:].as_matrix()
print(">>LandMarks")
print(landMarks)
print()

landMarks = landMarks.astype('int').reshape(-1, 2)
print(">>New LandMarks are:")
print(landMarks)
print()


path = "faces/{}".format(imageName)
image = io.imread(path)
print(image)

plt.imshow(image)
plt.title(imageName)

print("***************************************")
print(landMarks[:, 0])
print("***************************************")
print(landMarks[:, 1])

plt.scatter(landMarks[:, 0], landMarks[:, 1], s=20, marker=".", c='r')
plt.show()







