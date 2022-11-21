import random

with open("random.txt","w",encoding="UTF-8") as file:
    for i in range(50):
        file.write(str(random.randint(100,999)))
        file.write("\n")
file.close