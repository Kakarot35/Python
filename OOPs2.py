class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))

        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
            print(f"New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
            print(f"New Balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Owner: {self.owner}")
        print(f"Balance: ${self.balance}")


# Create Object
account1 = BankAccount("Karan", 1000)

# Display Initial Balance
account1.display_balance()

# Deposit Money
account1.deposit()

# Display Updated Balance
account1.display_balance()

# Withdraw Money
account1.withdraw()

# Display Final Balance
account1.display_balance()