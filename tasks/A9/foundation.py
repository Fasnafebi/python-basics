print("Daily Diary")
thought = input("Enter your thoughts: ")

with open("diary.txt", "a") as file:
    file.write(thought + "\n")

print("Your thoughts have been saved to diary.txt")
