from pathlib import Path
import time
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent
FORGE_GREETER = BASE_DIR.parent/"forge-greeter/forge-greeter.py"

 #Debugging: Check if the file exists
 #print(FORGE_GREETER.exists())  # This will print True if the file exists, False otherwise

def projects_menu():

    while True:
        print("\n" + "=" * 15)
        print("Projects Menu")
        print("=" * 15)

        print("\n1. Forge Greeter")
        print("2. Back")

        choice = input("\nPlease choose an option (1-2): ").strip()

        if choice == "1":
            run_forge_greeter()
        elif choice == "2":
            return  # Return to the main menu
        
        else:
            print("That is not a valid option. \nPlease choose between 1-2." )

def run_forge_greeter():

    if not FORGE_GREETER.exists():
        print("Forge Greeter script not found.")
        input("\nPress Enter to return to the Projects menu...")
        return
    subprocess.run([sys.executable, str(FORGE_GREETER)])