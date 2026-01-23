'''Create a class BankAccount that demonstrates encapsulation.

Requirements:

Balance should be private

Provide methods to:

Deposit money

Withdraw money

Check balance '''

class BankAccount:
    
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(5000)

acc.deposit(2000)
acc.withdraw(1500)

print("Current Balance:", acc.get_balance())
