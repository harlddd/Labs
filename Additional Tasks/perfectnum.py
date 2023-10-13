lower_value = int(input("Enter the starting number of the range: "))
upper_value = int(input("Enter the ending number of the range: "))
 
for n in range(lower_value, upper_value+1):
    sum = 0

    for i in range(1, n):
        if n%i == 0:
            sum += i
  

    if n == sum:
        print(n)