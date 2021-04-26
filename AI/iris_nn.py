import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'iris_dataset', 'iris.csv'))
X = df[['x0', 'x1', 'x2', 'x3', 'x4']]      # values from columns with specific header
Y = df[['type']]

mapping = {'Iris-virginica': np.array([1, 0, 0]),
           'Iris-versicolor': np.array([0, 1, 0]),
           'Iris-setosa': np.array([0, 0, 1])}

Y = np.array([mapping[y[0]] for y in Y.values])
X = X.values/9      # нормализация, деление всех признаков на самый большой


X_train = np.array([*X[0:40], *X[50:90], *X[100:140]])
Y_train = np.array([*Y[0:40], *Y[50:90], *Y[100:140]])

X_test = [*X[40:50], *X[90:100], *X[140:150]]
Y_test = [*Y[40:50], *Y[90:100], *Y[140:150]]

print(len(X_train), len(Y_train))
print(len(X_test), len(Y_test))

W = np.random.rand(5, 3)
print(W.shape)

a = 0.001
for epoch in range(1, 200):
    for i, X_row in enumerate(X_train):
        y_cappa = Y_train[i]
        y_experiment = np.array(X_row).dot(W)
        E = np.sqrt((y_cappa[0] - y_experiment[0])**2 + (y_cappa[1] - y_experiment[1])**2 + (y_cappa[2] - y_experiment[2])**2)
        for i in range(0, W.shape[1]):
            for j in range(0, W.shape[0]):
                de_dw = (2*(y_cappa[i] - y_experiment[i])*X_row[j]*(-1))/(2*E)
                W[j][i] = W[j][i] - a*de_dw
    print(E)

print('[INFO] Learning is finished\n')
count = 0
for i, X_row in enumerate(X_test):
    label = Y_test[i]
    y_experiment = np.array(X_row).dot(W)
    if np.argmax(y_experiment) == np.argmax(label):
        count += 1
    print(label, y_experiment)

print(count/len(X_test)*100)




