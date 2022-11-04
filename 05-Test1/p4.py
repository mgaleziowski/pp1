def f(number, even):
    sum=0
    nr=str(number)
    if(even):
        for i in range(len(nr)):
            if(int(nr[i])%2==0):
                sum+=int(nr[i])
    else:
        for i in range(len(nr)):
            if(int(nr[i])%2==1):
                sum+=int(nr[i])
    return sum
                
print(f(352,False))