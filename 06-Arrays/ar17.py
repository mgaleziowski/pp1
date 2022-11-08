import random
b=[1,5,9]
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
for i in range(10):
    for j in range(3):
        if(a[i]==b[j]):
            a[i]="n"
for z in range(10):
    if(a.count("n")>0):
        a.remove("n")
print(a)
    