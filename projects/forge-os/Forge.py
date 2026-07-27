import time

def show_menu():
    print("\n" + "=" * 15)
    print("Project Forge")
    print("=" * 15)

    print("\n1. Notes")
    print("2. Projects")
    print("3. Memory")
    print("4. Utilities")
    print("5. Exit")

def handle_choice(choice):
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
        time.sleep(2)  # Simulate loading time
        return False  
        # Exit the loop
    else:
        print("That is not a valid option. \nPlease choose between 1-5.")

    time.sleep(2)  # Simulate loading time
    return True  # Continue the loop

    
                                                                    
while True:
    show_menu()
    choice = input("\nPlease choose an option (1-5): ").strip()
    if not handle_choice(choice):
        break