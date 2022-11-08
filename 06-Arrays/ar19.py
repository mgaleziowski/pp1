import random
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
b=[]
for i in range(10):
    if(a.count(a[i])==1):
        b.append(a[i])
print(b)