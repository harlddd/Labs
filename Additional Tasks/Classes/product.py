class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def value(self):
        return self.price * self.quantity
    
    def add_items(self, quantity):
        self.quantity += quantity
    
    def remover(self, quantity):
        if quantity > self.quantity:
            print("Insufficient quantity")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

prod = Product("MacBookPro", 1000, 5)
print(prod.value()) 
prod.add_items(2)
print(prod.quantity)      
prod.remover(3)
print(prod.quantity)     
prod.remover(5)
print(prod)      