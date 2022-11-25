import re

text="crane, teeth, speaks, dream, creepy"
x=re.findall("c.{3}e",text)
print(x)