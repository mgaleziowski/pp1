import random
import bubble

a=[]
for r in range(3):
    a.append([])
    for g in range(5):
        a[r].append(random.randint(1,9))
bubble.array2d(a)
for v in range(3):
    help=a[v][0]
    a[v][0]=a[v][4]
    a[v][4]=help
print()
bubble.array2d(a)
