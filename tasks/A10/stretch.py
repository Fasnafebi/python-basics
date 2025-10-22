print("File Reader")

while True:
    filename = input("Enter filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"File contents: {content}")
            break 
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        choice = input("Would you like to try another file? (y/n): ").lower()
        if choice != 'y':
            print("Exiting File Reader.")
            break
