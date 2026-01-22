''' Design a Bank System where:

Parent class → Bank

Child class → SBI

Both have a method interest_rate()

Child class overrides parent method '''

class Bank:
    def interest_rate(self):
        print("bank interest rate is 5%")

class SBI(Bank):
    def interest_rate(self) :
        print("SBI interest rate is 7%")       

b = Bank()  
b.interest_rate()      

s = SBI()
s.interest_rate()