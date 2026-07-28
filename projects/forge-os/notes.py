import time

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
NOTES_FILE = BASE_DIR / "notes.txt"

def notes_menu():
    while True:
        print("\n" + "=" * 15)
        print("Notes")
        print("=" * 15)

        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = input("\nPlease choose an option (1-4): ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        elif choice == "4":
            return
        else:
            print("That is not a valid option.")
            print("Please choose between 1 and 4.")
            

def add_note():
    note = input("Write your note:").strip()

    if note == "":
        print("Note cannot be empty.")
        time.sleep(2)  # Simulate loading time
        return
    
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Note added successfully!")
    input("\nPress Enter to return to the Notes menu...")
    
def view_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

    except FileNotFoundError:
        print("\nNo notes have been saved yet.")
        time.sleep(2)
        return
    
    if not notes:
        print("\nNo notes have been saved yet.")
        time.sleep(2)
    else:
        print("\n" + "=" *15)
        print("\nYour Notes:")
        print("=" * 15)
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note.strip()}")
        input("\nPress Enter to return to the Notes menu...")

def delete_note():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

    except FileNotFoundError:
        print("\nNo notes have been saved yet.")
        input("\nPress Enter to return...")
        return

    if not notes:
        print("\nNo notes have been saved yet.")
        input("\nPress Enter to return...")
        return

    print("\n" + "=" * 15)
    print("Delete Note")
    print("=" * 15)

    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note.strip()}")

    choice = input(
        "\nEnter the number of the note to delete, or press Enter to cancel: "
    ).strip()

    if choice == "":
        return

    if not choice.isdigit():
        print("\nPlease enter a valid number.")
        time.sleep(2)
        return

    note_number = int(choice)

    if note_number < 1 or note_number > len(notes):
        print("\nThat note number does not exist.")
        time.sleep(2)
        return

    deleted_note = notes.pop(note_number - 1)

    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        file.writelines(notes)

    print(f"\nDeleted: {deleted_note.strip()}")
    input("\nPress Enter to return to the Notes menu...")
