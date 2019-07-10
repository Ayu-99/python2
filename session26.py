# In classification we need to predict about it belongs to which group
# we need more than one classes
# regression is predicting continuous data
# classification is prediction of class labels or what is the category

# Decision Trees
from sklearn.datasets import load_iris
# load iris is a dataset in scikit
from sklearn import tree

# 1.Create Data

irisData = load_iris()
print("=========Iris dataset=======")
print(irisData)
print(type(irisData))

print()

# Array of Features
print(irisData.data)

print()

# Array of targets
print(irisData.target)

print()

# Array of Target names
print(irisData.target_names)


# 2.Lets create Model
model = tree.DecisionTreeClassifier()

# 3. Train the Model| Supervised Learning
model.fit(irisData.data, irisData.target)

# 4. Lets Test our model !!
inputData = [4.6, 3.4, 1.4, 0.3]  # Versicolor type of iris flower

predictedClass = model.predict([inputData])

print("Predicted class is:", predictedClass)
print("Predicted class is:", predictedClass[0])
print("Predicted class is:", irisData.target_names[predictedClass[0]])

# Export our Data as graph visual!
import graphviz
data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATASET TREE")
graph.view()

# Explore : Gini Index and Chi square w.r.t Tree
