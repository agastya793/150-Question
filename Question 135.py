# exception handling
# ATM PIN VALIDATION

def check_pin(pin):
    try:
        if pin != 1234:
            raise ValueError("wrong pin")
        print("access granted")
    except ValueError as e:
        print(e)  

check_pin(4322)          
                             