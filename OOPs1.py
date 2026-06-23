class Mobile:
    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def call(self):
        print(f"{self.brand} is calling")
    def charge(self):
        print(f"{self.brand} is charging")

mobile1 = Mobile("Samsung", "Galaxy S21", 799)
mobile2 = Mobile("Apple", "iPhone 13", 999)

print(f"Mobile 1: {mobile1.brand} {mobile1.model} - ${mobile1.price}")
print(f"Mobile 2: {mobile2.brand} {mobile2.model} - ${mobile2.price}")

mobile1.call()
mobile2.charge()