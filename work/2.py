class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "woof")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "meow")

class Cow(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "moo")

dog = Dog("Dog")
dog.make_sound()  

cat = Cat("Cat")
cat.make_sound()  

cow = Cow("Cow")
cow.make_sound()  