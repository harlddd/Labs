
i = 0
d = i

while i < 100:
    i = i+1
    d = i**2
    if d > 2000:
        break
    print("Number:", i, "Square:", d)