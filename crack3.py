from string import ascii_lowercase
from itertools import product

for passcode in product(ascii_lowercase, repeat=8):
    print("".join(passcode))
