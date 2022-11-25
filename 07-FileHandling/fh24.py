import re

text="To be, or not to be, that is the question"
x=re.findall("a|e|o|u|i",text)
print(len(x))