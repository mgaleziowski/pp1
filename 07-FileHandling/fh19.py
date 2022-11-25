with open("integers.txt","w") as file:
    for i in range(1,51):
        file.write(f"{i}\n")

file.close