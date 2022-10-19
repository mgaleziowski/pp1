def digits(x):
    x=str(x)
    result=0
    for a in range(len(x)):
        result+=int(x[a])
    return result

n=input("podaj liczbe ")
print(f"suma cyfr wynosi {digits(n)}")