
while(1>0):
    try:
        nr=float(input("podaj liczbe "))
        break
    except:
        print("niepoprawna wartosc ")
        continue
if(((nr>=0.0)and(nr<=1.0))==False):
    gr="liczba poza zakresem "
elif(nr>=0.9):
    gr=5.0
elif(nr>=0.8):
    gr=4.5
elif(nr>=0.7):
    gr=4.0
elif(nr>=0.6):
    gr=3.5
elif(nr>=0.5):
    gr=3.0
else:
    gr=2.0
print(gr)
