def create_2d_arr(x,y):
    a=[]
    p=1
    q=1
    for xi in range(x):
        a.append([])
        for yi in range(y):
            a[xi].append(str(p*q))
            p+=1
        q+=1
        p=1
    for i in range(x):
        print(" ".join(a[i]))

create_2d_arr(10,10)