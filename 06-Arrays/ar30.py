def rand_elem(a):
    import random
    return a[random.randint(0,len(a)-1)]

print(rand_elem([1,2,3]))