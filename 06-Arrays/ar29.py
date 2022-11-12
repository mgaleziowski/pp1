import random

logic=True
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
b=[]
for r in range(3):
    b.append(random.randint(1,10))
print(b)
for i in range(3):
    if(a.count(b[i])==0):
        logic=False
print(logic)