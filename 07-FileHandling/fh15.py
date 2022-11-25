with open("15.txt","r",encoding="UTF-8") as file:
    list=[]
    for x in file:
        list.append(x)
    file.close
for i in range(len(list)):
    if(i%5==0):
        input("")
    print(list[i],end="")

