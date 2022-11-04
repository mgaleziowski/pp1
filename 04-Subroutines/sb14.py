kg=float(input("podaj swoja wage w kg "))
m=float(input("podaj swoj wzrost w metrach "))
bmi=lambda x,y: x/y**2
print(f"twoje bmi wynosi {bmi(kg,m)}")