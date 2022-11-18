def create_2d_arr(x,y):
    a=[]
    for xi in range(x):
        a.append([])
        for yi in range(y):
            a[xi].append("0")
    for xj in range(x):
        print(" ".join(a[xj]))
    
