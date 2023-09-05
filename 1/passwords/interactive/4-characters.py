from string import ascii_letters, digits, punctuation

password = input("Password: ")

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                guess = i + j + k + l
                if guess == password:
                    print(f"Cracked:  {guess}")
                    exit()
                else:
                    print(f"Cracking: {guess}", end="\r")
