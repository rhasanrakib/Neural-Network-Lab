import numpy as np
import time as tm


def train(weight, learn, target,epoch, **kargs):
    actual_output = 0
    error = 0
    weight_change = 0
    len_kargs = 0
    bias = 0
    
    for k in range(epoch):
        bias_accumulator=0
        weight_accumulator=0
        for i in kargs:
            len_kargs = len(kargs[i])
            for j in range(len_kargs):

                # print("weight = ", weight)
                bias_accumulator += learn*error
                actual_output = (weight.dot(kargs[i][j]))+bias
                error = target[j]-actual_output[0][0]
                #weight_change = learn*error*kargs[i][j]
                weight_change = np.transpose(learn*error*kargs[i][j])
                weight_accumulator+=weight_change
        weight=weight_accumulator
        bias=bias_accumulator
        print(f"weight = {weight},bias = {bias} ")

if __name__ == "__main__":
    p1 = np.array([[1], [2]])
    p2 = np.array([[2], [1]])
    p3 = np.array([[2], [3]])
    p4 = np.array([[3], [1]])
    weight = np.array([[0, 0]])
    target = [4, 5, 7, 7]

    # print(p2[1][0])
    train(weight=weight, learn=0.01, target=target, kargs=[p1, p2, p3, p4],epoch=1)
