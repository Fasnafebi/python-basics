filename = "highscores.txt"
scores = []
try:
    with open(filename, "r") as file:
        for line in file:
            if ": " in line:
                name, score = line.strip().split(": ")
                scores.append((name, int(score)))
except FileNotFoundError:
    pass  

print("High Scores Tracker")
print("Current high scores:")
for i, (name, score) in enumerate(scores, start=1):
    print(f"\t{i}\t{name}: {score}")

name = input("Enter your name: ")
score = int(input("Enter your score: "))
scores.append((name, score))

scores.sort(key=lambda x: x[1], reverse=True)
with open(filename, "w") as file:
    for name, score in scores:
        file.write(f"{name}: {score}\n")

print("Score saved!")
print("Updated high scores:")
for i, (name, score) in enumerate(scores, start=1):
    print(f"\t{i}\t{name}: {score}")
