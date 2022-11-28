import json

film={
"Title":"Five Feet Apart",
"Director":"Justin Baldoni",
"Release Date":"Mar7 2019",
"Genre":"Romance",
"Main Cast":["Haley Lu Richardson","Cole Sprouse","Moises Arias"]
}
file=open("favoritemovie.json","w")
json.dump(film,file,indent=4)

file.close