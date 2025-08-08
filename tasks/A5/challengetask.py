shopping_list = []

print("Shopping List Manager")

while True:
    print("\n\t1\tAdd item")
    print("\t2\tRemove item")
    print("\t3\tShow list")
    print("\t4\tCheck item")
    print("\t5\tExit")

    choice = input("Choice: ")

    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(f"Added '{item}' to the list!")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed '{item}' from the list!")
        else:
            print(f"'{item}' is not in the list.")

    elif choice == "3":
        if shopping_list:
            print("Current Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"\t{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        item = input("Enter item to check: ")
        if item in shopping_list:
            print(f"'{item}' is in the shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")

    elif choice == "5":
        print("Exiting Shopping List Manager.")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")