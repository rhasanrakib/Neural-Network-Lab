import numpy as np

bias = 0
w = np.array([1, 2])
p1 = np.array([[1],[2]])
p2 = np.array([[2], [1]])
p3 = np.array([[2], [3]])
p4 = np.array([[3], [1]])
net = [w.dot(p1)+bias, w.dot(p2)+bias, w.dot(p3)+bias, w.dot(p4)+bias]
for i in net:
    print(i)
