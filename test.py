def avg(*args):
    sum=0
    print(args)
    k=len(args)
    for i in args:
        sum+=i
    avg = sum//k
    return avg

a=avg(1,2,3,4)
print(a)