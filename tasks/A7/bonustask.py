import random
import string

def generate_password(length, include_numbers=True, include_symbols=True):
    letters = string.ascii_letters  
    numbers = string.digits         
    symbols = string.punctuation    

    characters = letters
    if include_numbers:
        characters += numbers
    if include_symbols:
        characters += symbols

    if not characters:
        return "Error: No characters selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if len(password) < 6:
        return "Weak"
    elif score == 4 and len(password) >= 12:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Generator")
    length = int(input("Length: "))
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_numbers, include_symbols)
    strength = check_strength(password)

    print(f"Generated password: {password}")
    print(f"Password strength: {strength}")

main()