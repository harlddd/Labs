import time

print("This is a shape calculator.")


while True:
    try: 
        time.sleep(1)
        length = int(input("Please enter the length of the rectangle: "))
        if length >0:
            break
        else:
            time.sleep(1)
            print("Number must be greater than 0")
        
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")
 
while True:
    try: 
        time.sleep(1)
        width = int(input("Please enter the width of the rectangle: "))
        if length >0:
            break
        else:
            time.sleep(1)
            print("Number must be greater than 0")
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")

        
perimeter = length*2 + width*2
area = length*width

   
time.sleep(1)
print("The perimeter is:", perimeter)
time.sleep(1)
print("The area is:", area)
time.sleep(1)
print(f"The perimeter is: {perimeter}")
time.sleep(1)
print(f"The area is: {area}")