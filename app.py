import random
import string


def generate_password(length, use_digits=False, use_symbols=False):
    symbols = string.ascii_letters

    if use_digits:
        symbols += string.digits
    if use_symbols:
        symbols += string.punctuation

    password = "".join(random.choice(symbols) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Довжина пароля: "))

    use_digits = input("Додати цифри? (y/n): ") == "y"
    use_symbols = input("Додати символи? (y/n): ") == "y"

    password = generate_password(length, use_digits, use_symbols)

    print("Пароль:", password)