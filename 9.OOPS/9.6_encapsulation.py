class Bank():
    def __init__(self, account_number, balance):
        self.account_number = account_number #public variable
        self.__balance = balance #private variable

    def deposite(self, amount):
        self.__balance += amount
        print(f'₹{amount} Amount Deposited in \nAccount no:{self.account_number}\nNew Balance:{self.__balance}')
    
    def get_balance(self):
        return self.__balance

a1 = Bank('12345',5000)
a1.deposite(2000)
print(a1.get_balance())
# print(a1.__balance) can't access directly