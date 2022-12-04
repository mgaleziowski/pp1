def f(age,course,avg):
    import json
    count=0
    with open("test.json","r",encoding="UTF-8") as file:
        data=json.load(file)
    for i in data:
        if(i["age"]>=age):
            for j in i["studies"]["courses"]:
                if(j["name"]==course):
                    grades=0
                    for x in j["grades"]:
                        grades+=x
                    if(grades/len(j["grades"])>=avg):
                            count+=1
    return count

