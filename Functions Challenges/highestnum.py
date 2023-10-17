def highestnum(a, b, c):
	if a > b and a > c:
		print(f"{a} is the highest number.")
	elif b > a and b > c:
		print(f"{b} is the highest number.")
	else:
		print(f"{c} is the highest number.")


while True:
	try:
		highestnum(int(input("1. ")), int(input("2. ")), int(input("3. ")))
		break
	except ValueError:
		print("Enter a valid value.")