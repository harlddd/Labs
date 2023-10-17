def oddeven(x):
	if x % 2 == 0:
		print(f"{x} is even")
	else:
		print(f"{x} is odd")

while True:
	try:
		x = int(input("Enter a number: "))
		break
	except ValueError:
		print("Please enter a valid value.")

oddeven(x)
