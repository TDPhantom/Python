class Person:
    species = "Homosapien"
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def hi(self):
     print("Hi my name is" + self.name)


Ansumana = Person("Ansumana", 17)
print(Ansumana.species)
print(Ansumana.name)
print(Ansumana.age)
Ansumana.hi()

Kalyn = Person("Kalyn", 17)
print(Kalyn.species)
print(Kalyn.name)
print(Kalyn.age)
Kalyn.hi()

# Class Inheritance: Inheritance allows us to define a class that inherits all the m othods and properties from another class

class Teacher(Person):
    role = 'teacher'

forlenza = Teacher("Forlenza , 184")
print(forlenza.role)

forlenza.hi