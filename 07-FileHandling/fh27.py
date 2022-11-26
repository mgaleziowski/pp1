import re
import bubble

with open("grades.txt","r",encoding="UTF-8") as file:
    text=file.read()
x=re.findall("(\d\.\d)",text)
print(bubble.mean(x))

file.close
