def compare(array1,array2):
    if(len(array1)==len(array2)):
        for i in range(len(array1)):
            if(array1[i]!=array2[i]):
                return False
    else:
        return False
    return True
a=[1,2,3,5]
b=[1,2,3,5]
print(compare(a,b))