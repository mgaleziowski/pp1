import random

ar=[]
for i in range(10):
    ar.append(random.randint(1,10))
max=ar[0]
min=ar[0]
for x in range(1,10):
    if(ar[x]>max):
        max=ar[x]    
    if(ar[x]<min):
        min=ar[x]
print(ar)
print(f"najwieksza to {max} a najmniejsza to {min}")