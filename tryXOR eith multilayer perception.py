def activation(n):
    return 1 if n>0 else 0

def calculate_eqn(input1,input2,weight,bias):
   h1= activation(weight[0]*input1+weight[2]*input2+bias[0])
   h2= activation(weight[1]*input1+weight[3]*input2+bias[1])
   return activation(weight[4]*h1+weight[5]*h2+bias[2])
   



if __name__ == "__main__":

    _input = [int(x) for x in input("input: ").split()]
    _weight = [int(x) for x in input("weight: ").split()]
    _bias = [int(x) for x in input("bias: ").split()]

    y=calculate_eqn(_input[0],_input[1],_weight,_bias)
    print(y)

