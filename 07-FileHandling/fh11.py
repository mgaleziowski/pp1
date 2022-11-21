film_titles=["Titanic","Morbius","Minions","Jaws","Baby Driver"]
file=open("films.txt","w",encoding="UTF-8")
for i in range(5):
    file.write(film_titles[i])
    file.write("\n")
file.close