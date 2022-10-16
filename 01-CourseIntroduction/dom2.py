a=[]
sum=0
count=0
while(1>0):
    try:
        inp=input(">")
        if(inp=="koniec"):
            break
        else:
            el=int(inp)
    except:
        print("error")
        continue
    a.append(el)
    count+=1
    sum+=el
if(count==0):
    avg="nie ma sredniej"
else:
    avg=sum/count
print("ilosc to",count," suma to",sum," srednia to",avg)
if(count>0):
    min=a[0]
    max=a[0]
    for b in a:
        if(b<min):
            min=b
        if(b>max):
            max=b
    print("najmniejsza wartosc to",min," najwieksza wartosc to",max)
    
