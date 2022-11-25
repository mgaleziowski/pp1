import re

text="To be, or not to be, that is the question"
x=re.findall(" ",text)
print(len(x)+1)