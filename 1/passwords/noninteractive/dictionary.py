with open("dictionary.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    print(line)
