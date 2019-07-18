from sklearn.cluster import KMeans

data = [[100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500],
       ]

# We do not have labels in this algorithm
# labels = [0, 0, 0, 0, 1, 1, 1, 1]

targetNames = ["Car", "Bike"]

clusters = 2
model = KMeans(n_clusters=clusters)

# train the model
# We are not mentioning the labels
model.fit(data)
#
# predictions = model.predict(data)
# print(predictions)

sampleInput = [800, 1000]
predictedClass = model.predict([sampleInput])
print(predictedClass)

