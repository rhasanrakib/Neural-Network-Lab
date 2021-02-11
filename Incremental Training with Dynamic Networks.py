import numpy as np
import time as tm


def train(weight, learn, bias, target, initial, data):
    actual_output = 0
    error = []
    len_kargs = 0
    flag = False
    for i in range(len(data)):
        p = np.array([[data[i]], [initial]])
        actual_output = (weight.dot(p))+bias
        error = target[i]-actual_output[0]
        del_weight = np.transpose(learn*error*p)
        weight = del_weight+weight
        print(
            f"actual output = {actual_output[0]},error = {error} ")
        initial=data[i]

if __name__ == "__main__":
    pi = 1
    p = [2, 3, 4]
    bias = 0
    weight = np.array([0, 0])
    target = [3, 5, 7]

    # print(p2[1][0])
    train(weight=weight, learn=0.1, bias=bias,
          target=target, initial=pi, data=p)
