name=input(">")
lines=0
with open(name,"r",encoding="UTF-8") as file:
    for x in file:
        lines+=1
    file.close
print(lines)