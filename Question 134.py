# QUESTION ON EXCEPTION HANDLING
# BANK BALANCE CHECK 

try:
    balance = 40000
    withdraw = int(input("Enter amount: "))
    if withdraw > balance:
        raise Exception("Insufficient funds")
    
    print("Transaction successful")
except Exception as e:
    print("error:", e)    
