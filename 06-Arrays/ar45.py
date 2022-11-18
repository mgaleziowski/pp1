import random
import bubble

a=[]
for r in range(3):
    a.append([])
    for g in range(5):
        a[r].append(random.randint(1,9))
bubble.array2d(a)
print()
b=[]
for i in range(3):
    for j in range(5):
        b.append(str(a[i][j]))
print(" ".join(b))
