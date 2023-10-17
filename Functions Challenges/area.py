def area(radius):
	area = 3.14*radius*radius
	return area
while True:
	try:
		radius = float(input("Please enter the radius of the circle: "))
		break
	except ValueError:
		print("Please enter a valid value.")

print(f"{area(radius):.2f}")