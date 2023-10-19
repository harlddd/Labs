class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity
    
    def add_items(self, quantity):
        self.quantity += quantity
    
    def remove_items(self, quantity):
        if quantity > self.quantity:
            print("Insufficient quantity")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

prod = Product("MacBookPro", 1000, 5)
print(prod.total_value()) 
prod.add_items(2)
print(prod.quantity)      
prod.remove_items(3)
print(prod.quantity)     
prod.remove_items(5)
print(prod)      