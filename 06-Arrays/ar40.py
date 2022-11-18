a=[[-38,19],[5,40],[-7,11],[29,16]]
max=a[0][0]
min=a[0][0]
maxad=[0,0]
minad=[0,0]
for i in range(4):
    for j in range(2):
        if(a[i][j]>max):
            max=a[i][j]
            maxad=[i,j]
        elif(a[i][j]<min):
            min=a[i][j]
            minad=[i,j]
print(f"najwieksza wartosc to: [{max}] w adresie: {maxad}")
print(f"najmniejsza wartosc to: [{min}] w adresie: {minad}")