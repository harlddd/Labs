import time

min = 1
max = 100
i = 3
while i >0:
        try: 
            time.sleep(1)
            guess = int(input("Please enter a value: "))
            if guess <= 0:
                print("Value must be between 1 and 100")
                i = i-1 
            elif guess > 100:
                print("Value must be between 1 and 100") 
                i = i-1 
            else:
                time.sleep(1)
                print(guess)
                break
                       
        except ValueError:
            time.sleep(1)
            print("Value must be a valid integer.")
            i = i-1 

if i == 0:
     print("None")

