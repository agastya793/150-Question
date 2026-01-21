''' Create a class Mobile with:

brand

model

price '''

class Mobile:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        
# Creating object of Mobile class
m1 = Mobile("Samsung", "Galaxy S23", 75000)

# Calling function
m1.display_details()
