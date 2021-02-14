import math 
def neuron(x,w,b,target,learn):
    z=0
    error=0
    while True:
        l = len(x)
        for i in range(l):
            z += x[i]*w[i]
        z+=b
        z=sigmoid(z)
        error=target-z
        del_weight= learn
    

def sigmoid(z):
    return 1/(1+math.exp(-1*z))

if __name__ == "__main__":
    b=0.1
    target=10
    learn = 0.1
    x=[5.1,5.1,5.1,5.1]
    w=[1.1,0.2,0.5,4]
    neuron(x,w,b,target,learn)
    