with open("15.txt","r") as file:
    with open("15copy.txt","w") as copy:
        copy.write(file.read())
    file.close
    copy.close