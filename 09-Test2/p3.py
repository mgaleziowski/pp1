def f(a2d):
    out=[]
    for i in a2d:
        sum=0
        for j in i:
            sum+=j
        out.append(sum)
    return out