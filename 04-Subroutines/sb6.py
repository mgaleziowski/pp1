def numpad(x):
    a=0
    for i in range(3):
        for y in range(1,4):
            print(y+a,end=" ")
        a+=3
        y=0
        print()
        
numpad(1)