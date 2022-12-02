def f(first,last):
    import re
    command=r'\bf\w*l\b'
    command=list(command)
    command[2]=first
    command[6]=last
    command="".join(command)
    with open("test.txt","r") as file:
        text=file.read()
    find=re.findall(command,text)
    return len(find)

def f2(first,last,text):
    import re
    command=r'\bf\w*l\b'
    command=list(command)
    command[2]=first
    command[6]=last
    command="".join(command)
    return re.findall(command,text)