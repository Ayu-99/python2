import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, metrics

digits = datasets.load_digits()
print(digits)
print("======================================")
print(digits.images)
print("======================================")
print(digits.images[0])
print("======================================")
print(digits.target_names)
print("======================================")
print(digits.target)
#
# plt.subplot(2, 4, 1)
# plt.imshow(digits.images[0], cmap=plt.cm.gray_r)
#
#
plt.subplot(2, 4, 2)
plt.imshow(digits.images[4], cmap=plt.cm.gray_r)

#
# for i in range(1, 5):
#     plt.subplot(2, 4, i)
#     plt.imshow(digits.images[i], cmap=plt.cm.gray_r)

plt.show()


X = digits.data
Y = digits.target

model = svm.SVC(gamma='scale')
model.fit(X, Y)

inputSample = digits.data[4]


predictedClass = model.predict([inputSample])

print(">> Predicted Class is:",predictedClass)

