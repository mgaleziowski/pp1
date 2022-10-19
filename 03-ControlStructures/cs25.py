while(1>0):
   a=int(input("podaj wysokosc "))
   b=int(input("podaj dlugosc "))
   if(a>=3 and b>=3):
       break
   else:
       print("zle dane ")
       continue
c=str("")
for z in range(b-2):
    c=c+" "
for x in range(b):
    print("*",end="")
print()
for y in range(a-2):
    print(f"*{c}*")
for v in range(b):
    print("*",end="")
    