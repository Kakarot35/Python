# OOP Fundamentals: Class Practice

# Define a class named "Pen" with the following attributes and methods:

class Pen:

    def __init__(self, color, brand, is_Working, type):
        self.color = color
        self.brand = brand
        self.is_Working = is_Working
        self.type = type

pen1 = Pen("Black", "Cello", False, "GelPoint" )

print(pen1.color)
print(pen1.brand)
print(pen1.is_Working)
print(pen1.type)