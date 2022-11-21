file=open("countries.txt","r")
line=1
for x in file:
    print(f"[{line}] {x}")
    line+=1
file.close