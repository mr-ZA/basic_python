import numpy as np

# train_X_data = np.random.randint(2, size=(10, 5, 20))
# train_Y_data = np.random.randint(2, size=(10, 2))

# train_Y_data = np.array([[1, 0], [1, 0], [0, 1], [0, 1]])
# train_X_data = np.array([[[1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#                         [[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#
#                         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
#                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
#                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]],
#                          [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
#                           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
#                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
#                           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]]
#                          ])




def sigmoid(x):
    return 1 / (1 + np.exp(-1 * x))


def forward(X, Ker, W_1, W_2, W_3):
    #print(X.shape, Ker.shape)
    vector = []
    for column_index in range(len(X[0])):
        column = X[:, column_index]
        vector.append(np.sum(np.multiply(column, Ker[column_index])))
    # for x in X:
    #     vector.append(np.array(x))

    l_1 = []
    for w1 in W_1:
        l_1.append(sigmoid(np.sum(np.multiply(vector, w1))))

    l_2 = []
    for w2 in W_2:
        l_2.append(sigmoid(np.sum(np.multiply(l_1, w2))))

    l_3 = []
    s = 0
    for w3 in W_3:
        s += np.exp(np.sum(np.multiply(l_2, w3)))
    for w3 in W_3:
        a = np.exp(np.sum(np.multiply(l_2, w3)))
        l_3.append(a/s)
    return np.array(l_3), np.array(l_2), np.array(l_1), np.array(vector)


def result_delta(y, y_predicted):
    return -np.sum(np.multiply(y, np.log(y_predicted)) + np.multiply((1 - y), np.log(1 - y_predicted)))


def W3_update_matrix(t, y, h, W_3, alpha):
    _row_len, _column_len = W_3.shape
    _matrix = []
    for i in range(_row_len):
        _row = []
        for j in range(_column_len):
            dE_dw = (t[i] - y[i]) * h[j]
            _row.append(-alpha * dE_dw)
        _matrix.append(_row)
    return np.array(_matrix)


def W2_update_matrix(t, y, h, input_layer, W_2, W_3, alpha):
    _row_len, _column_len = W_2.shape
    _matrix = []
    for j in range(_row_len):
        _row = []
        for k in range(_column_len):
            dE_dw = 0
            for i in range(len(t)):
                dE_dw += (y[i] - t[i]) * W_3[i][j] * h[j] * (1 - h[j]) * input_layer[k]
            _row.append(-alpha * dE_dw)
        _matrix.append(_row)
    return np.array(_matrix)


def W1_update_matrix(t, y, h, input_layer, x, W_1, W_2, W_3, alpha):
    _row_len, _column_len = W_1.shape
    _matrix = []
    # print(f'k:{len(input_layer)}')
    # print(f'l:{len(x)}')
    # print(f'j:{len(h)}')
    for l in range(len(x)):
        _row = []
        for k in range(len(input_layer)):
            s = 0
            for j in range(len(h)):
                inner_s = 0
                for i in range(W_3.shape[0]):
                    inner_s += y[i]*(1-t[i])*W_2[i][j]
                s += h[j]*(1-h[j])*inner_s*W_2[j][k]*input_layer[k]*(1-input_layer[k])*x[k]
            _row.append(-alpha * s)
        _matrix.append(_row)
    return np.array(_matrix)


def Kernel_update(t, y, h2, h1, x, x_raw, K, W_1, W_2, W_3, alpha):
    i = len(y)
    j = len(h2)
    k = len(h1)
    l = len(x)
    w = len(x_raw)
    # print(i, j, k, l, w)
    _matrix = []
    for row_num in range(w):
        _row = []
        for column_num in range(l):
            s = 0
            for kth in range(k):
                j_sum = 0
                for jth in range(j):
                    i_sum = 0
                    for ith in range(i):
                        i_sum += y[ith]*(1-t[ith])
                    j_sum += i_sum*h2[jth]*(1-h2[jth])*W_2[jth][kth]
                #print(W_1.shape)
                s += j_sum*h1[kth]*(1-h1[kth])*W_1[kth][column_num]
            dE_dk = s*x_raw[row_num][column_num]
            _row.append(dE_dk)
        _matrix.append(_row)
    return np.array(_matrix)


def backward(X, Y, L_3, L_2, L_1, V_, W_3, W_2, W_1, _kernel, alpha):
    # count errors
    d = result_delta(Y, L_3)
    # print(d)
    W_3_delta = W3_update_matrix(Y, L_3, L_2, W_3, alpha)
    W_2_delta = W2_update_matrix(Y, L_3, L_2, L_1, W_2, W_3, alpha)
    W_1_delta = W1_update_matrix(Y, L_3, L_2, L_1, V_, W_1, W_2, W_3, alpha)
    kernel_delta = Kernel_update(Y, L_3, L_2, L_1, V_, X, _kernel, W_1, W_2, W_3, alpha)

    # update weights (alpha and minus already in delta)
    W_3_updated = W_3 - W_3_delta
    W_2_updated = W_2 + W_2_delta
    W_1_updated = W_1 - np.transpose(W_1_delta)
    _kernel_updated = _kernel - np.transpose(kernel_delta)

    return W_3_updated, W_2_updated, W_1_updated, _kernel_updated,d


def main(train_x_data, train_y_data):
    kernel = 2 * np.random.rand(train_x_data.shape[2], 5) - 1
    W1 = 2 * np.random.rand(16, train_x_data.shape[2]) - 1
    W2 = 2 * np.random.rand(6, 16) - 1
    W3 = 2 * np.random.rand(2, 6) - 1
    for epoch in range(100):
        E = 0
        for i, train_x in enumerate(train_x_data):
            L3, L2, L1, V = forward(train_x, kernel, W1, W2, W3)
            W3, W2, W1, kernel, error = backward(train_x, train_y_data[i], L3, L2, L1, V, W3, W2, W1, kernel, 0.5)
            E += error
        if epoch % 10 == 1:
            print(E / 10)
    return kernel, W1, W2, W3
