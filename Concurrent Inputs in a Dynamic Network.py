import numpy as np
def net(*args):
    #print(args)
    #print(type(args))
    weight = [[1,2]]
    bias= 0
    lst1 = []
    lst2 = []
    lst3 = []
    for i in args:
        lst1.append([i[0]])
        lst2.append([i[1]])
            
    #print(lst1)
    for i in range(len(lst1)):
        temp =[]
        if i==0:
            temp.append(lst1[i])
            temp.append([0])
            lst3.append(temp.copy())
            temp.clear()
            temp.append(lst2[i])
            temp.append([0])
            lst3.append(temp.copy())
            temp.clear()
        else:
            temp.append(lst1[i])
            temp.append(lst1[i-1])
            lst3.append(temp.copy())
            temp.clear()
            temp.append(lst2[i])
            temp.append(lst2[i-1])
            lst3.append(temp.copy())
            #print(lst3)
            temp.clear()
    result=[]
    
    for i in lst3:
        result.append(matrix_multiplication(weight,i))
        #a=np_array(weight.dot(i))

    count=0
    final = []
    temp =[]    
    for i in range(len(result)):
        count+=1
        if count==1:
            temp.append(result[i][0][0]+bias)
        if count==2:
            count=0
            temp.append(result[i][0][0]+bias)
            final.append(temp.copy())
            temp.clear()
    print(final)
    

def matrix_multiplication(A,B):
    rowA =len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    #print(len(B))
    if colA == rowB:
        #result matrix will be rowA*colB
        result = []
        for i in range(rowA):
            temp =[]
            for j in range(colB):
                temp.append(0)
            result.append(temp.copy())
            temp.clear()
        
        
        for i in range(rowA):
            for j in range(colB):
                for k in range(rowB):
                    result[i][j] += A[i][k] * B[k][j]
        return result
        
    else:
        return "Not Possible"

if __name__ == "__main__":

    p1 = [1, 4]
    p2 = [2, 3]
    p3 = [3, 2]
    p4 = [4, 1]
    
    net(p1,p2,p3,p4)
    #train(weight=w,bias=bias,kargs=[p1,p2,p3,p4])
    #print(result)