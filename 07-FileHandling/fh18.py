with open("MeatAndFish.txt","r") as file1:
    list1=[]
    for x in file1:
        list1.append(x)
with open("GrainsAndBread.txt","r") as file2:
    list2=[]
    for y in file2:
        list2.append(y)
with open("shoppinglist.txt","w") as shop:
    for i in range(len(list1)):
        shop.write(list1[i])
    shop.write("\n")
    for j in range(len(list2)):
        shop.write(list2[j])

file1.close
file2.close
shop.close


    

