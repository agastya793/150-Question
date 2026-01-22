'''  Shopping Cart Total
 Task:

Calculate total price after discount.  '''



def total_price(price,discount):
    final = price- (price * discount / 100)
    return final

print("final price:", total_price(2000,20))