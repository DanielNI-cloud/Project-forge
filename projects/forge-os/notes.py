import time
from storage import load_notes, save_notes

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
    
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    
    print("Note added successfully!")
    input("\nPress Enter to return to the Notes menu...")
    
def view_notes():
    notes = load_notes()
    
    if not notes:
        print("\nNo notes have been saved yet.")
        time.sleep(2)
    else:
        print("\n" + "=" *15)
        print("\nYour Notes:")
        print("=" * 15)
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note}")
        input("\nPress Enter to return to the Notes menu...")

def delete_note():
    notes = load_notes()

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

    save_notes(notes)

    print(f"\nDeleted: {deleted_note}")
    input("\nPress Enter to return to the Notes menu...")
