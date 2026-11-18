from abc import ABC,abstractmethod

class Payment (ABC):
    def payment_details(self,amount):
        print("Payment startted")
        print("The amount is ",amount)

    @abstractmethod
    def pay(Self,amount):
        pass


class Google_pay(Payment):
    def pay(self,amount):
        self.payment_details(amount)
        print("paid using google pay")


class Phone_pay(Payment):
    def pay(self,amount):
        self.payment_details(amount)
        print("paid using Phone Pe")

obj1=Google_pay()
obj1.pay(1000)
print("--------------------------------------")
obj2=Phone_pay()
obj2.pay(2000)
