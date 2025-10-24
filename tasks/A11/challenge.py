import random
import string

def generate_password(length, use_upper, use_numbers, use_symbols, exclude_similar):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    all_chars = lower + upper + numbers + symbols

    
    if exclude_similar:
        for ch in "0O1lI":
            all_chars = all_chars.replace(ch, "")

    if not all_chars:
        return None

    
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def analyze_password(password, use_upper, use_numbers, use_symbols):
    length = len(password)
    strength_points = 0

    print("Password Analysis:")
    
    if length < 8:
        print("❌ Length: Weak (less than 8 characters)")
    elif length <= 12:
        print(f"✅ Length: Moderate ({length} characters)")
        strength_points += 1
    else:
        print(f"✅ Length: Strong ({length} characters)")
        strength_points += 2

    
    if any(ch.isupper() for ch in password):
        print("✅ Uppercase: Yes")
        strength_points += 1
    else:
        print("❌ Uppercase: No")
    
    
    if any(ch.islower() for ch in password):
        print("✅ Lowercase: Yes")
        strength_points += 1
    else:
        print("❌ Lowercase: No")
    
    
    if any(ch.isdigit() for ch in password):
        print("✅ Numbers: Yes")
        strength_points += 1
    else:
        print("❌ Numbers: No")

    
    if any(ch in string.punctuation for ch in password):
        print("✅ Symbols: Yes")
        strength_points += 1
    else:
        print("❌ Symbols: No")

    
    if strength_points <= 2:
        strength = "Weak"
    elif strength_points <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"🔒 Overall strength: {strength}")

print("Advanced Password Generator")


while True:
    try:
        length = int(input("Password length (8-50): "))
        if 8 <= length <= 50:
            break
        else:
            print("Please enter a number between 8 and 50.")
    except ValueError:
        print("Please enter a valid number!")

use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
exclude_similar = input("Exclude similar characters (0,O,l,1)? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_numbers, use_symbols, exclude_similar)

if password:
    print(f"\nGenerated password: {password}")
    analyze_password(password, use_upper, use_numbers, use_symbols)
else:
    print("Error: No character sets selected!")
