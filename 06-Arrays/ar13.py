import random
a=[]
for i in range(10):
    a.append(random.randint(1,10))
print(a)
for x in range(10):
    a[x]*=a[x]
print(a)