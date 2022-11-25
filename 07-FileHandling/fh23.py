import re

text="Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
x=re.findall("\d{2}",text)
sum=0
for i in range(3):
    sum+=int(x[i])
print(sum/3)