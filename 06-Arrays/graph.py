import bubble

graph=[]
n=int(input("size>"))
low=int(input("low>"))
high=int(input("high>"))
func=input("func>")
for y in range(n):
    graph.append([])
    for x in range(n):
        graph[y].append("□")
for i in range(n):
    for j in range(n):
        if(j>low and j<high and bubble.abs(i-(eval(func)))<1):
            graph[i][j]="■"
for a in range(0,n-1):
    if(graph[a+1].count("■")==0):
        graph[a+1]=graph[a]
for r in range(n-1,-1,-1):
    print(" ".join(graph[r]))

        