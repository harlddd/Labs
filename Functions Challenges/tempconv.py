while True:
    try:
        degrees = float(input("Enter temp in Celcius: "))
        break
    except ValueError:
        print("Please enter a valid value.")

def fahrenheit(degress):
    converted = (degrees * 1.8) + 32
    return(f"{degrees} Celcius is equivalent to {converted} in Fahrenheit.")

print(fahrenheit(degrees))