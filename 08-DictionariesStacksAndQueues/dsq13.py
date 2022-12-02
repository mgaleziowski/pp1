import json
student={
"imie":"Mikolaj",
"nazwisko":"Galeziowski",
"wiek":19,
"przedmioty":["matematyka","informatyka","angielski","niemiecki","zarzadzanie"]
}
with open("student.json","w") as file:
    json.dump(student,file,indent=4)
file.close
