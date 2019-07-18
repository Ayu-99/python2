import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print("=====", tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(len(train_images))
print(len(test_images))

print("========Training Images[0]===========")
print(train_images[0])

print("========Testing Images[0]============")
print(test_images[0])


plt.subplot(2, 4, 1)
plt.imshow(train_images[0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(test_images[0], cmap=plt.cm.gray_r)

plt.show()