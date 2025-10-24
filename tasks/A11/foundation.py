import random

def roll_die(sides=6):
    return random.randint(1, sides)

def roll_multiple_dice(count, sides):
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls, sum(rolls)

def menu():
    print("\nDice Roller")
    print("\t1\tRoll a 6-sided die")
    print("\t2\tRoll a 20-sided die")
    print("\t3\tRoll multiple dice")
    print("\t4\tExit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        result = roll_die(6)
        print(f"🎲 You rolled: {result}")

    elif choice == "2":
        result = roll_die(20)
        print(f"🎲 You rolled: {result}")

    elif choice == "3":
        try:
            count = int(input("How many dice? "))
            sides = int(input("Number of sides on each die (e.g., 6, 10, 20): "))
            if count <= 0 or sides <= 0:
                print("Error: Please enter numbers greater than 0!")
            else:
                rolls, total = roll_multiple_dice(count, sides)
                print("🎲" * count, f"You rolled: {', '.join(map(str, rolls))} Total: {total}")
        except ValueError:
            print("Error: Please enter a valid number!")

    elif choice == "4":
        print("Exit")
        break

    else:
        print("Invalid option! Please select from 1 to 4.")
