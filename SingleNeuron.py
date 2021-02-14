import numpy as np
def activation_function(z):
    return max(z,0)


def train(weight, learn, target, **kargs):
    actual_output = 0
    error = 0
    weight_change = 0
    len_kargs = 0
    flag = False
    ep=30
    while ep:
        for i in kargs:
            len_kargs = len(kargs[i])
            for j in range(len_kargs):
                mul = (weight.dot(kargs[i][j]))
                actual_output = activation_function(mul[0][0])
                error=target[j]-mul[0][0]
                print(
                    f"weight  = {weight}, actual output = {actual_output}")
                weight_change = learn*error*kargs[i][j]
                weight_change = np.transpose(weight_change)
                weight = weight + weight_change
                
        ep-=1


if __name__ == "__main__":
    p1 = np.array([[1], [2]])
    p2 = np.array([[2], [1]])
    p3 = np.array([[2], [3]])
    p4 = np.array([[3], [1]])
    weight = np.array([[0, 0]])
    target = [4, 5, 7, 7]
    bias=0.1
    # print(p2[1][0])
    train(weight=weight, learn=0.1, target=target,kargs=[p1, p2, p3, p4])
