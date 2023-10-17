while True:
    print("Time Calculator")
    print("1. Add 2 times")
    print("2. Find the difference between 2 times")
    print("3. Convert to Hours")
    print("4. Convert to Minutes")
    print("5. Convert Minutes to time")
    print("6. Convert Hours to time")
    print("7. Convert Days to time")
    print("8. Exit")
    
    choice = input("Enter an option: ")
    
    if choice == "1":
        while True:
            time1 = input("Enter your first time (in format DD:HH:MM): ")
            split1 = time1.split(':')
            if len(split1) == 3 and 0 <= int(split1[0]) < 1000 and 0 <= int(split1[1]) < 24 and 0 <= int(split1[2]) < 60:
                break
            else:
                print("Incorrect value entered. Please enter time in the format DD:HH:MM. The maximum days is 1000.")
        while True:
            time2 = input("Enter your second time (in format DD:HH:MM): ")
            split2 = time2.split(':')
            if len(split2) == 3 and 0 <= int(split2[0]) < 1000 and 0 <= int(split2[1]) < 24 and 0 <= int(split2[2]) < 60:
                break
            else:
                print("Incorrect value entered. Please enter time in the format DD:HH:MM. The maximum days is 1000.")
        split1 = time1.split(':')
        split2 = time2.split(':')
        days = int(split1[0]) + int(split2[0])
        hours = int(split1[1]) + int(split2[1])
        minutes = int(split1[2]) + int(split2[2])
        if minutes >= 60:
            minutes -= 60
            hours += 1
        if hours >= 24:
            hours -= 24
            days += 1
        print(f"The sum of {time1} and {time2} is {days}:{hours}:{minutes}")
    elif choice == "2":
        time1 = input("Enter time 1 (in format DD:HH:MM): ")
        time2 = input("Enter time 2 (in format DD:HH:MM): ")
        split1 = time1.split(':')
        split2 = time2.split(':')
        days = int(split1[0]) - int(split2[0]) 
        hours = int(split1[1]) - int(split2[1]) 
        minutes = int(split1[2]) - int(split2[2]) 
        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            hours += 24
            days -= 1
        if days < 0:
            split1, split2 = split2, split1
            days = -days
            hours = -hours
            minutes = -minutes
            if minutes < 0:
                minutes += 60
                hours -= 1
            if hours < 0:
                hours += 24
                days -= 1
        print(f"The difference between {time1} and {time2} is {days}:{hours}:{minutes}")

    elif choice == "3":
        time = input("Enter time in the format DD:HH:SS: ")
        split1 = time.split(':')
        total_minutes = int(split1[0]) * 1440 + int(split1[1]) * 60 + int(split1[2])
        total_hours = total_minutes // 60
        print(f"The total hours in {time} is {total_hours}")

    elif choice == "4":
        time = input("Enter time in the format DD:HH:SS: ")
        split1 = time.split(':')
        total_minutes = (int(split1[0]) * 1440 + int(split1[1]) * 60 + int(split1[2]))
        print(f"The total minutes in {time} is {total_minutes}")

    elif choice == "5":
        total_minutes = int(input("Enter total minutes: "))
        days = total_minutes // 1440
        hours = (total_minutes % 1440) // 60
        minutes = total_minutes % 60
        print(f"The time in {total_minutes} minutes is {days}:{hours}:{minutes}")

    elif choice == "6":
        total_hours = int(input("Enter total hours: "))
        days = total_hours // 24
        hours = total_hours % 24
        minutes = 0
        print(f"The time in {total_hours} hours is {days}:{hours}:{minutes}")
    elif choice == "7":
        total_days = int(input("Enter total days: "))
        days = total_days
        hours = 0
        minutes = 0
        print(f"The time in {total_days} days is {days}:{hours}:{minutes}")
    elif choice == "8":
        break
    else:
        print("Invalid input. Please try again.")
