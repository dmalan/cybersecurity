from string import ascii_letters

password = input("Password: ")

for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                guess = i + j + k + l
                if guess == password:
                    print(f"Cracked:  {guess}")
                    exit()
                else:
                    print(f"Cracking: {guess}", end="\r")
