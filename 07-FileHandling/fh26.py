import re

text="crane, teeth, speaks, dream, creepy, tracksuit"
x=re.findall("\w{6,}",text)
print(len(x))