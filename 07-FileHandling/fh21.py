import random

with open("numbers1to10.txt","w",encoding="UTF-8") as file:
    for i in range(3,15):
        for j in range(2,5):
            file.write(str(i**j))
            file.write(", ")
        file.write("\n")
file.close
