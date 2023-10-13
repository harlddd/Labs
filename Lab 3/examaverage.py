import time

value = range(100)

for i in value:
    try:   
        maths = int(input("Please enter the maths grade: "))
        if maths >0 and maths <=100: 
            break
        else:
            print("Value must be between 0 and 100")
    except ValueError:
        print("Please enter a valid integer.")

for i in value:
    try:
        english = int(input("Please enter the english grade: "))
        if english >0 and english <=100: 
            break
        else:
            print("Value must be between 0 and 100")
    except ValueError:
        print("Please enter a valid integer.")

for i in value:
    try:
        it = int(input("Please enter the IT grade: "))
        if it >0 and it <=100: 
            break
        else:
            print("Value must be between 0 and 100")
    except ValueError:
        print("Please enter a valid integer.")

average = (maths + english + it) /3

print(f"Youre average was {average}")
if average >= 65:
    print("Pass")
else:
    print("Fail")



''''
while True:
    try: 
        time.sleep(1)
        maths = int(input("Please enter the maths grade: "))
        if maths >0 and maths <=100:
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
        english = int(input("Please enter the english grade: "))
        if english >0 and english <=100:
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
        it = int(input("Please enter the IT grade: "))
        if it >0 and it <=100:
            break
        else:
            time.sleep(1)
            print("Grade must be between 1 and 100")
        
    except ValueError:
        time.sleep(1)
        print("Grade must be a valid integer.")
 
average = (maths + english + it) /3

print(average)
'''