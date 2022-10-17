while(1>0):
    x=float(input("podaj wspolrzedna x "))
    y=float(input("podaj wspolrzedna y "))
    if(x*y==0):
        print("punkt na osi")
        continue
    else:
        break
q=0
if(x>0):
    if(y>0):
        q=1
    else:
        q=4
elif(y>0):
    q=2
else:
    q=3
print("w",q,"kwadracie")