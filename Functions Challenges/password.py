def password_checker(password):
	x = ["password123", "password01", "admin", "12345"]
	if password in x:
		print(f"Use a safer password! {password} is compromised")
	else: 
		print(f"{password} is ok to use!")
		
password = input("Enter a password to check: ")
password_checker(password)