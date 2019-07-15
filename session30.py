from sklearn import svm
# X = [[0, 0], [1, 1]]
# Y = [0, 1]
# model = svm.SVC(gamma='scale')
# model.fit(X, Y)
# inputSample = [1, 2]
# predictedClass = model.predict([inputSample])
# print(predictedClass)

data = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500],
       ]

labels = [0, 0, 0, 0, 1, 1, 1, 1]

model = svm.SVC(gamma='scale')
model.fit(data, labels)
inputData = [700, 1500]
predictedClass = model.predict([inputData])
print(">>", predictedClass)