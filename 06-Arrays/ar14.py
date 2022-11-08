a=["jan","sran","dzban","dzbaniarz"]
max=0
for i in range(1,len(a)):
    if(len(a[i])>len(a[max])):
        max=i
print(a[max])