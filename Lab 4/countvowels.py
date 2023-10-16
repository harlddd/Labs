i = str(input("Enter a word or sentence: "))

vowels = ["a", "e", "i", "o", "u"]
count = 0


for character in i:
    if character.lower() in vowels:
        count += 1

print("Number of vowels in the given string is: ", count)
