import random
import bubble
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
arr=list(set(a))
b=bubble.bubblesort(arr)
print(b[len(b)-2])
