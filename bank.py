class bank:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance or amount<0:
            print("Insufficient balance")
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
b=bank()
b.deposit(2000)
b.deposit(1000)
b.withdraw(500)
print(b.get_balance())
