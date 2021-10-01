import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
#print(df.head())

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x, y, test_size = 0.8)

classifier = neighbors.KNeighborsClassifier()
classifier.fit(xTrain, yTrain)

accuracy = classifier.score(xTest, yTest)

print('Accuracy ', accuracy)

example_data = np.array([2,1,2,1,2,1,3,1,2])
example_data = example_data.reshape(len(example_data), -1)

prediction = classifier.predict(example_data)
print(prediction)
