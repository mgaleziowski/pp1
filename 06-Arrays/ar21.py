import random
import ar18
a=[]
for r in range(10):
    a.append(random.randint(1,10))
print(a)
b=set(ar18.bubblesort(a,len(a)))
print(b[len(b)-2])
