import re


def ifrange(min,max,x):
    if(x>=min and x<=max):
        return True
    else:
        return False
    
a=int(input("podaj dolna granice "))
b=int(input("podaj gorna granice "))
n=int(input("podaj badana liczbe "))
if(ifrange(a,b,n)):
    print("liczba znajduje sie w zakresie")
else:
    print("liczba NIE znajduje sie w zakresie")