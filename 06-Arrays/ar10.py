import random

def sum(array):
    sum=0
    for i in range(10):
        sum+=array[i]
    return sum

def arr2str(array):
    return "".join(array)

a=[]
for i in range(10):
    a.append(random.randint(1,10))
print(a)    
print(sum(a))
print(arr2str(a))