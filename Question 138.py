# Method Overloading 
''' Design a Bill Calculator where:

If only price is given → return price

If price + quantity is given → return total

If price + quantity + discount is given → apply discount'''


'''Python does NOT support method overloading directly,
but we achieve it using:

✅ Default arguments
✅ *args'''

class Bill:
    def calculate(self,*args):
        if len(args) == 1:
            # only price
            return args[0]
        elif len(args) == 2:
            # price * quantity
            return args[0] * args[1]
        elif len(args) == 3:
            # PRICE * QUantity - discount
            price,qty,discount = args
            total = price * qty
            return total - (total * discount / 100)
        
        else:
            return "Invalid input"
        
b = Bill()

print("Bill 1:", b.calculate(100))
print("Bill 2:", b.calculate(100,3))
print("Bill 3:", b.calculate(100,3,10))