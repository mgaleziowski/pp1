def bubblesort(a,l):
    for x in range(l):
        for i in range(l-1):
            if(a[i]>a[i+1]):
                help=a[i+1]
                a[i+1]=a[i]
                a[i]=help
    return a