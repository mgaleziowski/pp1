a=[[0,0,0],[0,0,0],[0,0,0]]
j=0
for i in range(3):
    a[i][j]=1
    j+=1
for x in range(3):
    for y in range(3):
        a[x][y]=str(a[x][y])
print(" ".join(a[0]))
print(" ".join(a[1]))
print(" ".join(a[2]))