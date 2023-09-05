from string import digits

password = input("Password: ")

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                guess = i + j + k + l
                if guess == password:
                    print(f"Cracked:  {guess}")
                    exit()
                else:
                    print(f"Cracking: {guess}", end="\r")
