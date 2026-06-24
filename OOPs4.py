class Animal:
     def __init__(self, name):
          
          self.name = name
     
     def eat(self):
          print(f"{self.name} is eating" )
    
     def sleep(self):
          print(f"{self.name} is sleeping")

class Dog(Animal):
     def bark(self):
          print(f"{self.name} is barking")


dog1 = Dog("Tommy")

dog1.bark()
dog1.eat()
dog1.sleep()