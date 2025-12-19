# Random Password Generator
# Oasis Infobyte Internship Project
# Author: Nakka Gurusekhar

import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters  # a-z A-Z
    if use_numbers:
        characters += string.digits          # 0-9
    if use_symbols:
        characters += string.punctuation     # symbols

    if characters == "":
        return "Error: No character set selected!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0")
    else:
        letters = input("Include letters? (y/n): ").lower() == "y"
        numbers = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        result = generate_password(length, letters, numbers, symbols)
        print("\nGenerated Password:", result)

except ValueError:
    print("Invalid input! Please enter a number.")
