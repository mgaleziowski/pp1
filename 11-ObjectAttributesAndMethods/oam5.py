class Music():
    def __init__(self,artist,title,album,year):
        self.artist=artist
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
        return "Performer: "+self.artist+"\nSong: "+self.title+"\nAlbum: "+self.album+"\nYear: "+self.year
my_music=Music("Ed Sheeran","Hearts dont break around here","Divide","2017")
song1=Music("abc","piosenka","albumik","2069")
print(song1)
