import csv

with open("datacsv.csv","r") as file:
    row=csv.reader(file,delimiter=",")
    list=[]
    for x in row:
        list.append(x)
