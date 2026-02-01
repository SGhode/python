class Animal: # Parent class (superclass)
    location = "Japan"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")

class Dog(Animal): # This is how inheritance is done in python
    def speak(self):
        super().speak() # This is how inheritance is done in Python
        print("woof!")

# a = Animal("Dog")
# a.speak()     
d = Dog("Bruno")
d.speak()
# print(d.location)






