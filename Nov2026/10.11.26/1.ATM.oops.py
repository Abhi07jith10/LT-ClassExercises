#create a class ATM
#method 1 (details, balance=10000, name)
#method2 = deposit()
#method3 = withdrawl()
#method4 = check balance

class ATM():
    def details(self,balance,name):
        self.name=name
        self.balance=balance
        print(f"Hy {name} welcome to SBI BANK")
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        print(f"Hy your deposit is succesfull")
        print(f"Your account balance after deposit is {self.balance}")
    def withdraw(self,withdrawl_amount):
        if withdrawl_amount<=self.balance:
            self.balance-=withdrawl_amount
            print("withdrawl succesfull")
            print(F"Your account balance after withdrawl is {self.balance}")

        else:
            print("insufficient balance")
    def check_balance(self):
        print(f"Your balance amount is {self.balance}")

# Test it
acc = ATM()
acc.details(balance=10000,name="Abhi")
acc.deposit(2000)
acc.withdraw(5000)
acc.check_balance()    # Your balance is 7000
acc.withdraw(20000)    # Insufficient balance