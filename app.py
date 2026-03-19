import random
import string

length = int(input("Довжина пароля: "))

use_digits = input("Додати цифри? (y/n): ") == "y"
use_symbols = input("Додати символи? (y/n): ") == "y"

symbols = string.ascii_letters

if use_digits:
    symbols += string.digits
if use_symbols:
    symbols += string.punctuation

password = "".join(random.choice(symbols) for _ in range(length))

print("Пароль:", password)