from datetime import datetime, date

 
 
zodiac_animals = [
    "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
    "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
]


birthstones = {
    1: "Garnet", 2: "Amethyst", 3: "Aquamarine",
    4: "Diamond", 5: "Emerald", 6: "Pearl",
    7: "Ruby", 8: "Peridot", 9: "Sapphire",
    10: "Opal", 11: "Topaz", 12: "Turquoise"
}

print("Birthday Calculator")
birth_input = input("Enter your birth date (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    today = date.today()

    
    day_of_week = birth_date.strftime("%A")

    
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    
    if age_days < 0:
        age_months -= 1
        age_days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
    if age_months < 0:
        age_years -= 1
        age_months += 12

    
    days_lived = (today - birth_date).days

    
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    days_until_birthday = (next_birthday - today).days

    
    zodiac = zodiac_animals[birth_date.year % 12]

    
    birthstone = birthstones[birth_date.month]

    print("\n🎂 Birthday Facts:")
    print(f"\t• You were born on a {day_of_week}")
    print(f"\t• You are {age_years} years, {age_months} months, and {age_days} days old")
    print(f"\t• You have lived for {days_lived:,} days")
    print(f"\t• Your next birthday is in {days_until_birthday} days")
    print(f"\t• You were born in the year of the {zodiac} (Chinese zodiac)")
    print(f"\t• Your birthstone is {birthstone}")

except ValueError:
    print("Error: Please enter the date in correct format (YYYY-MM-DD).")
