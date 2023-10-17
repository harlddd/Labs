import time

def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif 11850 <= salary <= 34500:
        return (salary - 11850) * 0.2
    elif 34501 <= salary <= 150000:
        return 4530 + ((salary - 34500) * 0.4)
    else:
        return 50730 + ((salary - 150000)) * 0.45 

print("Welcome to the tax calculator")
time.sleep(0.5)

while True:
    try:
        time.sleep(0.5)
        salary = int(input("What is your salary? £"))
        break
    except ValueError:
        time.sleep(0.5)
        print("Please enter a valid value")

tax_amount = getIncomeTax(salary)
time.sleep(0.5)
print("Tax anmount for salary £{} is £{}".format(salary, tax_amount))