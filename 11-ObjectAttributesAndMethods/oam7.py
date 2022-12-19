class Student():
    uni="UEK"
    id=10**5
    def __init__(self,name,surname,field):
        self.name=name
        self.surname=surname
        Student.id+=1
        self.id=str(Student.id)
        self.field=field
    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nID: {self.id}\nField: {self.field}\n"
s1=Student("Anna","Maj","Applied informatics")
s2=Student("Lukasz","Doniec","Applied informatics")
print(s1)
print(s2)