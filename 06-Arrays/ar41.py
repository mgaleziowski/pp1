import random
import bubble

a=[]
for r in range(3):
    a.append([])
    for g in range(5):
        a[r].append(random.randint(1,9))
bubble.array2d(a)
print()
help=a[0]
a[0]=a[2]
a[2]=help
bubble.array2d(a)