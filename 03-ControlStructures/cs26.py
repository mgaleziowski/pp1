real=[0,8,0,5]
pin=[0,0,0,0]
print("podaj pin")
i=0
att=0
while(att<3):
    for x in range(4):
        pin[x]=(int(input(">")))
    while(i<4):
        if(pin[i]==real[i]):
            print(end="")
        else:
            corr=False
            break
        i+=1
        if(i==4):
            corr=True
    if(corr):
        print("pin prawidlowy")
        break
    else:
        print("pin nieprawidlowy")
        pin.clear
        att+=1
if(att==3):
    print("karta zablokowana")
        