from abc import ABC,abstractmethod


class Character(ABC):

    @abstractmethod
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword")

class Mage(Character):
    def attack(self):
        print("Mage attacks with magic")

class Archer(Character):
    def attack(self):
        print("Archer attacks with Bow")

warrior = Warrior()
mage = Mage()
Archer = Archer()

warrior.attack()
mage.attack()
Archer.attack()