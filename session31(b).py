from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris_data = load_iris()
features = iris_data.data
# print(features)


clusters = 3
model = KMeans(n_clusters=clusters)

# train the model
# We are not mentioning the labels
model.fit(features)

predictions = model.predict(features)
print(predictions)

# Use ur clustering on image DataSets