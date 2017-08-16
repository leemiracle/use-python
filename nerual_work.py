# coding=utf8
from collections import defaultdict
import numpy as np
import math


def sigmoid(u):
    return 1.0 / (1 + math.exp(-u))


def learn_single_unit():
    # Learning Algorithms for a Single Unit
    alpha = 0.01
    X = [0, 1, 2]
    W = [2, 1, 0]
    t = 1
    count = 0
    while(1):
        u = sum([X[i]*W[i] for i in X])
        # the logistic function (a most common kind of sigmoid function),

        # predict value
        y_1 = sigmoid(u)
        print(count, u, W, y_1)
        if y_1 == t:
            break
        W = [(v-alpha*(y_1-t)*y_1*(1-y_1))*X[i] for i, v in enumerate(W)]
        count += 1
    print(W)


def learn_multi_layer(alpha):
    # Back - propagation with Multi - Layer Network
    # size: input K is 3, hidden N is 2, output M is 4
    X = np.matrix([0, 1, 0])
    W_k_n = np.matrix([
        [1, 0],
        [0, 1],
        [0, 0]])
    W_n_m = np.matrix([
        [-5, 5, -5, -5],
        [-5, 5, -5, -5]])

    # 数组转置
    # W_i = []
    # for row in W_k_n:
    #     W_i_len = len(row)-len(W_i)
    #     if W_i_len > 0:
    #         for j in range(W_i_len):
    #             W_i.append([])
    #     for i in range(len(row)):
    #         W_i[i].append(row[i])
    # print W_i
    count = 0
    while 1:
        u_i = np.matmul(X, W_k_n).tolist()[0]
        h_N = u_i
        # h_N = map(sigmoid, u_i)

        h_N = np.matrix(h_N)
        print "h_N:", h_N

        y_m = np.matmul(h_N, W_n_m)
        y_m = y_m.tolist()[0]
        y_m = map(sigmoid, y_m)
        print y_m

        t = [0 for i in range(len(y_m))]
        t[1] = 1
        print "y_m", y_m
        if t == y_m:
            break

        E_j = []
        for i, y in enumerate(y_m):
            E_j.append(y * (1 - y) * (t[i] - y))
        print "E_j:", E_j

        W_n_m = W_n_m.tolist()
        h_N = h_N.tolist()[0]
        for i, w in enumerate(W_n_m):
            for j, a in enumerate(w):
                W_n_m[i][j] = W_n_m[i][j] - alpha * h_N[i] * E_j[j]
                print W_n_m[i][j]
        print "W_n_m:", W_n_m

        E_i = []
        for i, h in enumerate(h_N):
            tmp = []
            for j, E in enumerate(E_j):
                tmp.append(W_n_m[i][j] * E * h * (1 - h))
            E_i.append(sum(tmp))
        print "E_i:", E_i

        W_k_n = W_k_n.tolist()
        x_k = X.tolist()[0]
        for k, w in enumerate(W_k_n):
            for i, a in enumerate(w):
                W_k_n[k][i] = W_k_n[k][i] - alpha * x_k[k] * E_i[i]
        print "W_k_n:", W_k_n
        W_k_n = np.matrix(W_k_n)
        W_n_m = np.matrix(W_n_m)
        count += 1
        print "count", count

def main():
    alpha = 0.01
    sentence = ["abd", "abc", "acabd"]
    vacab = defaultdict(int)
    for w in sentence:
        for c in w:
            vacab[c] += 1
    print(vacab)
    # learn_single_unit()
    learn_multi_layer(alpha)



if __name__ == '__main__':
    main()
