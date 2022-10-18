for x in range(30):
    a=x+1
    if(a%3==0 and a%5==0):
        print("bingo",end=" ")
    elif(a%3==0):
        print("three",end=" ")
    elif(a%5==0):
        print("five",end=" ")
    else:
        print(a,end=" ")