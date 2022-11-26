import random

def count5(b):
    i=1
    j=0
    while(True):
        nr=random.randint(1,b)
        if(nr==i):
            if(i==b):
                break
            else:
                i+=1
        else:
            i=1
            j+=1
    return j

while(True):
    b=int(input(">"))
    if(b>0):
        break
min=10000
a=min
while(a>0):
    a=count5(b)
    if(a<min):
        min=a
        print(a)
        
