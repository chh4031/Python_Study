from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import numpy as np

digit = datasets.load_digits()
x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6)

p = Perceptron(max_iter = 100, eta0 = 0.001)
p.fit(x_train, y_train)

res = p.predict(x_test)
print(res)

conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]] += 1
print(conf)

correct = 0
for i in range(10):
    correct += conf[i][i]
accuracy = correct/len(res)
print("Accuracy is ", accuracy * 100, "%")