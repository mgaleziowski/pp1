with open("15.txt","r") as file:
    with open("15copy2.txt","w") as copy:
        for x in file:
            copy.write(x)
    file.close