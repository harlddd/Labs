file = open("teams.txt", "w")

teams = ["Lakers", "Heat", "Trailblazers", "Bulls", "Warriors"]

for i in teams:
    newline = i + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")

lines = file.readlines()

print(lines[0].strip())
print(lines[3].strip() + "\n")
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
file.close()
lines[0] = "New line"

file = open("teams.txt", "w")

for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else:
        file.write(lines[i].strip() + "\n")

file.close()

file = open("teams.txt", "r")

for line in file:
    print(line.strip())