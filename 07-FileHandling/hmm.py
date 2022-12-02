import re
text="crane, creepy, case"
a="c"
b="e"
command=r'\bf\w*l\b'
command=list(command)
command[2]=a
command[6]=b
command="".join(command)
print(re.findall(command,text))