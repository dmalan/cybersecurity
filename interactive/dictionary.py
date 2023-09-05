password = input("Password: ")

# Sort by length so that \r doesn't leave remnants of alphabetically earlier but longer guesses
with open("dictionary.txt", "r") as file:
    lines = sorted(file.read().splitlines(), key=len)

for guess in lines:
    if guess == password:
        print(f"Cracked:  {guess}")
        exit()
    else:
        print(f"Cracking: {guess}", end="\r")
