from types import resolve_bases


def sum(x):
    result=0
    for y in range(1,x+1):
        result+=y
    return result

n=int(input("podaj zakres [1;n] "))
print(f"suma liczb z zakresu jest rowna {sum(n)}")