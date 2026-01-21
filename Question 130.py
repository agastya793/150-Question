''' Electricity Bill Calculator
 Rules:
Units	Cost
First 100	₹5/unit
Next 100	₹7/unit
Above 200	₹10/unit'''

def electricity_bill(units) :
    if units <= 100:
        return units* 5
    elif units <= 200:
        return (100 * 5) + (units -100) * 7
    else:
        return(100*5) + (100 *7) + (units - 200) * 10
    
print("Bill:", electricity_bill(250))