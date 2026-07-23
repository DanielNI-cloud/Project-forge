while True:
    print("\n" + "=" * 15)
    print("Project Forge")
    print("=" * 15)

    print("\n1. Notes")
    print("2. Projects")
    print("3. Memory")
    print("4. Utilities")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ").strip()

    if choice == "1":
        print("Opening Notes...")
    # Add functionality for Notes here
    elif choice == "2":
        print("Opening Projects...")
    # Add functionality for Projects here
    elif choice == "3":
        print("Opening Memory...")
    # Add functionality for Memory here
    elif choice == "4":
        print("Opening Utilities...")
    # Add functionality for Utilities here
    elif choice == "5":
        print("Closing Project Forge...")
    # Add exit functionality here
    break
else:
print("That is not a valid option. Please choose (1-5).")