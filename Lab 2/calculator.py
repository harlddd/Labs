import time

print("This is a calculator.")

while True:
    try: 
        time.sleep(1)
        number1 = int(input("Please enter your first value: "))
        break
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")
 
while True:
    try: 
        time.sleep(1)
        number2 = int(input("Please enter your second value: "))
        break
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")

time.sleep(1)
print("Which operation would you like to choose? \n 1. Add + \n 2. Subtract - \n 3. Multiply * \n 4. Divide / \n 5. Square s")


while True:
    time.sleep(1)
    operation = str(input("Please select the desired operation: "))
    
    if operation == "1" or operation == "+":
        time.sleep(1)
        print(number1 + number2)
        break
    elif operation == "2" or operation == "-":
        time.sleep(1)
        print(number1 - number2)
        break
    elif operation == "3" or operation == "*":
        time.sleep(1)
        print(number1 * number2)
        break
    elif operation == "4" or operation == "/":
        time.sleep(1)
        print(number1 / number2)
        break
    elif operation == "5" or operation == "s":
        time.sleep(1)
        print(number1 ** number2)
        break
    else:
        time.sleep(1)
        print("Invalid Input")
   