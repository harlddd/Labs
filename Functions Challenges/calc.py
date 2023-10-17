def calc(x, y):
	sum = x + y
	sub = x - y
	mul = x * y
	print(f"sum is {sum}, sub is {sub}, multiply is {mul}")

while True:
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter a valid value.")
        
calc(x, y)