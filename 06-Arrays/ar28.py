import random

a=[]
for r in range(10):
    a.append(str(random.randint(1,999)))
print(a)
b="|".join(a)
print(f"|{b}|")

