def minmax(array):
    min=array[0]
    max=array[0]
    for i in range(1,len(array)):
        if(array[i]>max):
            max=array[i]
        if(array[i]<min):
            min=array[i]
    b=[min,max]
    return b

