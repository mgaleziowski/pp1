a=[0,1]
print("0 1 ",end="")
for x in range(2,50):
    a.append(a[x-1]+a[x-2])
    print(a[x],end=" ")