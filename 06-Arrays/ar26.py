import random

a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
even=[]
odd=[]
for i in range(10):
    if(a[i]%2==0):
        even.append(a[i])
    else:
        odd.append(a[i])
print(even+odd)

