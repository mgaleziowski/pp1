import random
import bubble

a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
a=bubble.bubblesort(a)
print(a[len(a)-1]-a[0])
