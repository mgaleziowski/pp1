def f(binary_number):
    nr=str(binary_number)
    for i in range(len(nr)):
        if(nr[i]!="0" and nr[i]!="1"):
            return False
    return True

b=input("podaj liczbe binarna ")
print(f(b))