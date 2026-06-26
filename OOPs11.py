from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("CreditCard payment successfull")
    
class UPI(Payment):
    def pay(self):
        print("Upi payment successfull")

class PayPal(Payment):
    def pay(self):
        print("PayPal payment successfull")

payments = [CreditCard(), UPI(), PayPal()]

for payment in payments:
    payment.pay()