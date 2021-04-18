import pandas as pd
import numpy as np

df = pd.read_csv('dataset/iris.csv')
X = df[['x0', 'x1', 'x2', 'x3', 'x4']]
Y = df[['type']]

mapping = {'Iris-virginica': np.array([1, 0, 0]),
           'Iris-versicolor': np.array([0, 1, 0]),
           'Iris-setosa': np.array([0, 0, 1])}

Y = np.array([mapping[y[0]] for y in Y.values])
X = X.values


X_train = [*X[0:40], *X[50:90], *X[100:140]]
Y_train = [*Y[0:40], *Y[50:90], *Y[100:140]]

X_test = [*X[40:50], *X[90:100], *X[140:150]]
Y_test = [*Y[40:50], *Y[90:100], *Y[140:150]]

print(len(X_train), len(Y_train))
print(len(X_test), len(Y_test))


def sigmoid(x):
    return 1/(1 + np.exp(-x))