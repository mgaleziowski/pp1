a=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
for i in range(4):
    for j in range(3):
        if(a[i][j]%2==0):
            sum+=a[i][j]
print(sum)