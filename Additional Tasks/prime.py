lower_value = int(input ("Enter the lower range: "))  
upper_value = int(input ("Enter the upper range: "))  
  
print ("Prime numbers within the listed range: ")  
for prime in range (lower_value, upper_value + 1):  
    if prime > 1:  
        for i in range (2, prime):  
            if (prime % i) == 0:  
                break  
        else:  
            print (prime)  