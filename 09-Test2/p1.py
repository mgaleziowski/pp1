def f(pl1,pl2):
    pl1=str(pl1)
    pl2=str(pl2)
    sum1=0
    sum2=0
    value={
    "Q":10,
    "K":10,
    "J":10,
    "A":10,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
    "1":1,
    "0":0
    }
    for i in pl1:
        sum1+=value[i]
    for j in pl2:
        sum2+=value[j]
    if(sum1>sum2):
        return True
    return False
    