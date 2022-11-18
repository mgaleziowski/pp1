import bubble
import random

a=[]
for r in range(3):
    a.append([])
    for g in range(5):
        a[r].append(random.randint(1,9))
bubble.array2d(a)
print("transpozycja:")
bubble.array2d(bubble.transpose(a))