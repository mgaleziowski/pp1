def bubblesort(a):
    for x in range(len(a)):
        for i in range(len(a)-1):
            if(a[i]>a[i+1]):
                help=a[i+1]
                a[i+1]=a[i]
                a[i]=help
    return a
