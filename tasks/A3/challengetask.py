secret_number = 8
tries = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    tries += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You won in {tries} tries.")
        break