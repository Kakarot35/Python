
from abc import ABC,abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("Dog is running.")

class Cat (Animal):
    def move(self):
        print("Cat is walking.")

class Bird (Animal):
    def move(self):
        print("Bird is flying.")


dog = Dog()
cat = Cat()
bird = Bird()

animals = [dog, cat, bird]

for animals in animals:
    animals.move()