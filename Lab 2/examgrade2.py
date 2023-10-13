import time

print("Welcome to the exam grade calculator!")

while True:
    try: 
        time.sleep(1)
        grade = int(input("Please enter the students grade: "))
        if grade >0 and grade <=100:
            break
        else:
            time.sleep(1)
            print("Grade must be between 1 and 100")
        
    except ValueError:
        time.sleep(1)
        print("Grade must be a valid integer.")
 

while True:
    try: 
        time.sleep(1)
        level = int(input("Please enter the students level: "))
        if level >0 and level <=2:
            break
        else:
            time.sleep(1)
            print("Level must be between 1 and 2")
        
    except ValueError:
        time.sleep(1)
        print("Level must be a valid integer.")

if level == 1:
    if grade < 50:
        print("Fail")
    elif grade < 61:
        print("Pass")
    elif grade < 71:
        print("Merit")
    else:
        print("Distinction")
else:
    if grade < 40:
        print("Fail")
    elif grade < 51:
        print("Pass")
    elif grade < 66:
        print("Merit")
    else:
        print("Distinction")
