import numpy as np

def sequentialInputsDynamicNetwork(weight,bias,**kargs):
    sum = []
    for i in kargs:
        #print(kargs[i])
        for j in range(len(kargs[i])):
            if j==0:
                kargs[i][j] = np.append(kargs[i][j],0)
                sum.append(weight.dot(kargs[i][j])+bias)
                
            else:
                kargs[i][j]  = np.append(kargs[i][j],kargs[i][j-1][0])
                sum.append([weight.dot(kargs[i][j])+bias])
                

    print(sum)

if __name__ == "__main__": 
    
    bias = 0
    w = np.array([[ 1,2]] )
    p1 = np.array([1])
    p2 = np.array([2])
    p3 = np.array([3])
    p4 = np.array([4])
    
    sequentialInputsDynamicNetwork(weight=w,bias=bias,kargs=[p1,p2,p3,p4])