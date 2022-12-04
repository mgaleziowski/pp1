def f(first,last):
    import re
    command=r'\bf\w*l\b'
    command=list(command)
    command[2]=first
    command[6]=last
    command="".join(command)
    with open("test.txt","r",encoding="UTF_8") as file:
        text=file.read()
    find=re.findall(command,text)
    return find

print(f("w","d"))