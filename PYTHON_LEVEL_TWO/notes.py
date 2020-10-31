class Dog():
    """
    Dog class
    """
    #class object attribute
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    
mydog=Dog(breed="Amstaff",name="Wiz")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
print(type(1))

class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self,new_r):
        self.radius = new_r

myc = Circle(3)
print(myc.radius)
myc.setRadius(100)
print(myc.area())