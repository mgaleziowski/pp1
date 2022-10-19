def month(x):
    if(x==1):
        return "january"
    elif(x==2):
        return "february"
    elif(x==3):
        return "march"
    elif(x==4):
        return "april"
    elif(x==5):
        return "may"
    elif(x==6):
        return "june"
    elif(x==7):
        return "july"
    elif(x==8):
        return "august"
    elif(x==9):
        return "september"
    elif(x==10):
        return "october"
    elif(x==11):
        return "november"
    elif(x==12):
        return "december"
    else:
        return "nie ma takiego miesiaca"

a=int(input("ktory numer miesiaca? "))
print(month(a))
      
    