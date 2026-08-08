import time

def projects_menu():

    while True:
        print("\n" + "=" * 15)
        print("Projects Menu")
        print("=" * 15)

        print("\n1. Forge Greeter")
        print("2. Back")

        choice = input("\nPlease choose an option (1-2): ").strip()

        if choice == "1":
            print(" Opening Forge Greeter...")
            time.sleep(2)  # Simulate loading time
            # Add functionality for Forge Greeter here
        
        elif choice == "2":
            return  # Return to the main menu
        
        else:
            print("That is not a valid option. \nPlease choose between 1-2.")
   