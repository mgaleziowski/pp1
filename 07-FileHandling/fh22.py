with open("data.txt","r",encoding="UTF-8") as file:
    list=[]
    for x in file:
        list.append(x)
for i in range(len(list)):
    list[i]=(str(list[i])).split(",")
for j in range(1,6):
    if(int(list[j][2])<30):
        print(f"{list[j][0]} {list[j][1]} {list[j][4]}",end="")

file.close
