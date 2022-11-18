a=[[True,False],[True,True],[False,False]]
for i in range(3):
    for j in range(2):
        a[i][j]=bool(1-int(a[i][j]))
print(a)
        