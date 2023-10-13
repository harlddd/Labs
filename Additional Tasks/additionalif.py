a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
c = int(input("Please enter your third number: "))

if a > b and a > c:
    if (a % 2) == 0:
        print("Even Number")
    elif (a % 3) == 0:
        print("Odd number and multiple of 3")
    else:
        print("Odd Number")
elif b > a and b >c:
    if (b % 2) == 0:
        print("Even Number")
    elif (b % 3) == 0:
        print("Odd number and multiple of 3")
    else:
        print("Odd Number")
elif c > a and c > b:
    if (c % 2) == 0:
        print("Even Number")
    elif (c % 3) == 0:
        print("Odd number and multiple of 3")
    else:
        print("Odd Number")