class Animal:

    def sound(self):
        pass

class Dog (Animal):

    def sound(self):
        print("Dog Bark.")

class Cat (Animal):

    def sound(self):
        print("Cat Meow.")

class Cow (Animal):

    def sound(self):
        print("Cow Moos.")

dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]

for animals in animals:
    animals.sound()
    