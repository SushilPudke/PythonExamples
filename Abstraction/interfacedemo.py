# Demonstrating interface
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit card payment of- ', amount)


class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)

obj = CreditCardPayment()
obj.payment(100)
print(isinstance(obj, Payment))
obj = MobileWalletPayment()
obj.payment(200)
print(isinstance(obj, Payment))