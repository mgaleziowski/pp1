import random

a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
b=int(input(">"))
count=0
for i in range(10):
    if(a[i]>b):
        count+=1
print(f"jest {count} elementow weikszych od [{b}]")
