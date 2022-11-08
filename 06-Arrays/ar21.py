import random
import bubble
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
c=list(set(bubble.bubblesort(a,len(a))))
b=bubble.bubblesort(c,len(c))
print(b[len(b)-2])
