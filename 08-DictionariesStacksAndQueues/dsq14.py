alphabet={
"a":"Alpha",
"b":"Beta",
"c":"Charlie",
"d":"Delta"
}
word=(input(">")).lower()
code=[]
for i in word:
    code.append(alphabet[i])
print(" ".join(code))
