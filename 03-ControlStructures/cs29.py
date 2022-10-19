count=0
sum=0
while(1>0):
    a=int(input(">"))
    if(a==0):
        break
    else:
        sum+=a
        count+=1
if(count>0):
    avgco="a srednia arytm. wynosi"
    avg=(sum/count)
else:
    avgco=""
    avg=""
print(f"wpisano {count} liczb, ich suma wynosi {sum} {avgco} {avg}")
