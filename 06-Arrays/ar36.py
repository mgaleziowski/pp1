import random

a=[]
for i in range(2):
    a.append([])
    for j in range(4):
        a[i].append(str(random.randint(1,10)))
for x in range(2):
    print(" ".join(a[x]))

