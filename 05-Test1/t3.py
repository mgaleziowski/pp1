def f(password):
    return (len(set(password))>=6)

print(f(input(">")))