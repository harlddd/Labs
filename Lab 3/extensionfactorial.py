


while True:
    try:
        input = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer")

d = 1

for i in range(input):
    d = d*input
    input = input-1
    print(d)

