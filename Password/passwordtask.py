import time

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def password_rating(self):
        uppercase = False
        lowercase = False
        numberchar = False
        specialchar = False
        for char in self.password:
            if char.isupper():
                uppercase = True
            elif char.islower():
                lowercase = True
            elif char.isnumeric():
                numberchar = True
            elif not char.isalnum():
                specialchar = True
        commonpass = ["password", "123456", "password01", "admin", "welcome", "hello"]
        if self.password in commonpass:
            return "\033[1;31mVery weak\033[0m"
        if len(self.password) < 8:
            return "\033[31mWeak\033[0m"
        elif len(self.password) < 12 and (not uppercase or not lowercase or not numberchar):
            return "\033[33mModerate\033[0m"
        elif len(self.password) < 12 and uppercase and lowercase and numberchar:
            return "\033[32mStrong\033[0m"
        elif len(self.password) < 16 and uppercase and lowercase and numberchar and specialchar:
            return "\033[32mStrong\033[0m"
        elif len(self.password) >= 16:
            return "\033[1;32mVery strong\033[0m"
        else:
            time.sleep(0.5)
            return "\033[33mModerate\033[0m"


history = {}

while True:
    time.sleep(0.5)
    passwordcheck = input("Enter a password: ")

    if passwordcheck in history:
        time.sleep(0.5)
        print(f"Password rating: {history[passwordcheck][-1]}")
    else:
        checker = PasswordChecker(passwordcheck)
        RATING = checker.password_rating()

        if passwordcheck not in history:
            history[passwordcheck] = []
        history[passwordcheck].append(RATING)
        time.sleep(0.5)
        print(f"Password rating: {RATING}")
    
    time.sleep(0.5)
    print("\033[34mYour password history:\033[0m")
    for passwordcheck, ratings in history.items():
        time.sleep(0.5)
        print(f"Password: {passwordcheck}")
        for rating in ratings:
            time.sleep(0.5)
            print(f" - Rating: {rating}")
    time.sleep(0.5)
    answer = input("Enter another password? (y/n): ")
    if answer.lower() != "y":
        break
