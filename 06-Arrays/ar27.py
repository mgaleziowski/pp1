def f(a):
    for i in range(len(a)):
        a[i]=str(a[i])
    return ",".join(a)
