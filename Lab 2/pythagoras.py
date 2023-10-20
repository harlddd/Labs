import time
import math

while True:
    try: 
        time.sleep(1)
        pythagoras = int(input("Pythagoras Calculator \n \t 1. Find the length of A given B and C \n \t 2. Find the length of B given A and C \n \t 3. Find the length of C given A and B \n Please choose an option: "))
        if pythagoras >0 and pythagoras <=3:
            break
        else:
            time.sleep(1)
            print("Value must be between 1 and 3")
                    
    except ValueError:
        time.sleep(1)
        print("Value must be a valid integer.")

if pythagoras == 1:
    while True:
        try:
            time.sleep(1)
            side1 = int(input("Please enter the length of side B: "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    while True:
        try: 
            time.sleep(1)
            side2 = int(input("Please enter the length of side C: "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    
    
    square = side2**2 - side1**2
    side3 = print(f"The length of side A is {math.sqrt(square)}")
    
elif pythagoras == 2:
    while True:
        try: 
            time.sleep(1)
            side1 = int(input("Please enter the length of side A: "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    while True:
        try: 
            time.sleep(1)
            side2 = int(input("Please enter the length of side C: "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    
    
    square = side2**2 - side1**2
    side3 = print(f"The length of side B is {math.sqrt(square)}")
else:
    while True:
        try: 
            time.sleep(1)
            side1 = int(input("Please enter the length of side A: "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    while True:
        try: 
            time.sleep(1)
            side2 = int(input("Please enter the length of side B "))
            if side1 >= 0:
                break
            else:
                time.sleep(1)
                print("Value must be above 0")
                        
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
    
    
    square = side2**2 + side1**2
    side3 = print(f"The length of side A is {math.sqrt(square)}")

                