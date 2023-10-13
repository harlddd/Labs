'''
invest = 100
while invest < 1000:
    invest = invest + (invest/10)
    print(invest)

'''
import time

while True:
    try: 
        time.sleep(1)
        i = int(input("Please enter the initial investment amount: "))
        if i >0:
            break
        else:
            time.sleep(1)
            print("Investment must be greater than 0")
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")

while True:
    try: 
        time.sleep(1)
        t = int(input("Please enter the target value: "))
        if t >i:
            break
        else:
            time.sleep(1)
            print("Target value must be greater than initial investment")
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")

while True:
    try: 
        time.sleep(1)
        r = int(input("Please enter the interest rate: "))
        if r >0:
            break
        else:
            time.sleep(1)
            print("Interest must be greater than 0")
    except ValueError:
        time.sleep(1)
        print("Please enter a valid integer.")


while i < t:
    i = i + (i*(r/100))
    #print(round(i, 2))
    print("%.2f" % i)