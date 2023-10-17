author = {'dave': ["bookw", "book 2"], 'keith': ["vooe2", "boows"], 'stevie': ["bigbook", "lilbook"]}

user = input("Please enter the name of the author: ")


if user == "dave":
    #author2 = "list of books by author: ".join(author)
    print(", ".join(author[user]))
elif user == "keith":
    print(", ".join(author[user]))
elif user == "stevie":
    print(", ".join(author[user]))
else:
    print("Not a known author")