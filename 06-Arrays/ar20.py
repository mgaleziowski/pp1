import random
a=[]
for r in range(10):
    a.append(random.randint(1,10))
while(True):
    b=int(input(">"))
    if(b==0):
        break
    else:
        print(f"[{b}] appears {a.count(b)} times")
print(a)