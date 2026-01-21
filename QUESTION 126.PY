''' 

Question:

Design a system for:

Bank Account

Deposit

Withdraw

Check Balance 
'''
class BankAccount:

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def deposit(self,amount)  :
        self.balance += amount
        print("deposited:", amount)  

    def withdraw(self,amount) :
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawn:", amount)   
        else:
            print("Insufficient balance")
    def check_balance(self)  :
        print("current Balance:", self.balance)      