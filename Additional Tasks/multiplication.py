number = int(input ("Enter the number of the multiplication table: "))      
limit = int(input("Enter how many values you would like from the table: "))

print ("The Multiplication Table of: ", number)   
 
for count in range(1, limit+1):      
   print (f"{number} x {count} = {number * count}")    