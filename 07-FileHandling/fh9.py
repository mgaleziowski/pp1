file=open("numbers.txt","r")
sum=0
for x in file:
    sum+=int(x)
print(sum)