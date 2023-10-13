
i = str(input("Enter a word or sentence: "))


count = len([char for char in i if char in "aeiouAEIOU"])

print("Number of vowels: ", count   )


'''
i = str(input("Enter a word or sentence: "))

vowels = ["a", "e", "i", "o", "u"]
count = 0


for character in i:
    if character in vowels:
        count += 1

print("Number of vowels in the given string is: ", count)
'''