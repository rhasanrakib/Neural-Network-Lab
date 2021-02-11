import numpy as np
import time as tm


def train(weight, learn, bias, target, initial, data, epoch):
    actual_output = 0
    error = []
    len_kargs = 0
    flag = False
    for j in range(epoch):
        accumulate_weight = np.array([0.0, 0.0])
        initial_value=initial
        for i in range(len(data)):
            
            p = np.array([[data[i]], [initial_value]])
            actual_output = (weight.dot(p))+bias
            error = target[i]-actual_output
            del_weight = np.transpose(learn*error*p)
            accumulate_sum=accumulate_weight+ del_weight
            accumulate_weight=accumulate_sum
            initial_value =data[i]
        weight = accumulate_weight
        print(f"{j+1} Epoch weight  = {weight}")


if __name__ == "__main__":
    pi = 1
    p = [2, 3, 4]
    weight = np.array([0, 0])
    target = [3, 5, 6]

    # print(p2[1][0])
    train(weight=weight, learn=0.02, bias=0,
          target=target, initial=pi, data=p, epoch=1)
