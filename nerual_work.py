# coding=utf8
from collections import defaultdict
import numpy as np
import math


def main():
    alpha = 0.01
    sentence = ["abd", "abc", "acabd"]
    vacab = defaultdict(int)
    for w in sentence:
        for c in w:
            vacab[c] += 1
    print(vacab)

    #  Learning Algorithms for a Single Unit
    # X = [0, 1, 2]
    # W = [2, 1, 0]
    # t = 1
    # count = 0
    # while(1):
    #     u = sum([X[i]*W[i] for i in X])
    #     # the logistic function (a most common kind of sigmoid function),
    #
    #     def f(u):
    #         return 1.0/(1+math.exp(-u))
    #     # predict value
    #     y_1 = f(u)
    #     print(count, u, W)
    #     if y_1 == t:
    #         break
    #     W = [(v-alpha*(y_1-t))*X[i] for i, v in enumerate(W)]
    #     count += 1
    # print(W)

    # Back - propagation with Multi - Layer Network
    # size: input K is 3, hidden N is 2, output M is 4
    X = np.matrix([0, 1, 2])
    W_k_n = np.matrix([
        [1, 2],
        [3, 4],
        [5, 6]])

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
    h_N = np.matmul(X, W_k_n)
    print h_N
    W_n_m = np.matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8]])
    y_m = np.matmul(h_N, W_n_m)
    y_m = y_m.tolist()[0]
    print y_m

    def f(u):
        return 1.0 / (1 + math.exp(-u))
    y_m = map(f, y_m)
    t = [0 for i in range(len(y_m))]
    t[0] = 1

    print y_m

if __name__ == '__main__':
    main()
