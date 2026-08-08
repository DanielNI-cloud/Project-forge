import time
from storage import load_notes, save_notes

def notes_menu():
    while True:
        print("\n" + "=" * 15)
        print("Notes")
        print("=" * 15)

        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Back")

        choice = input("\nPlease choose an option (1-5): ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_notes()

        elif choice == "4":
            delete_note()
            
        elif choice == "5":
            break
        else:
            print("That is not a valid option.")
            print("Please choose between 1 and 5.")
            

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
        display_notes(notes)
        input("\nPress Enter to return to the Notes menu...")

def delete_note():
    notes = load_notes()

    if not notes:
        print("\nNo notes have been saved yet.")
        time.sleep(2)
        return

    print("\n" + "=" * 15)
    print("Delete Note")
    print("=" * 15)

    display_notes(notes)

    print("=" * 15)
    print("Delete Note")
    print("=" * 15)

    note_index = select_note(notes)
    if note_index is None:
        return

    deleted_note = notes.pop(note_index)

    save_notes(notes)

    print(f"\nDeleted: {deleted_note}")
    input("\nPress Enter to return to the Notes menu...")

def display_notes(notes):
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")

def select_note(notes):
 
    while True:
        choice = input(
        "\nEnter the number of the note, or press Enter to cancel: ").strip()

        if choice == "":    
            return None 

        if not choice.isdigit():
            print("\nPlease enter a valid number.")
            time.sleep(3)
            continue

        note_number = int(choice)

        if note_number < 1 or note_number > len(notes):
            print("\nThat note number does not exist.")
            time.sleep(3)
            continue

        return note_number-1   

def search_notes():
    notes = load_notes()

    if not notes:
        print("\nNo notes have been saved yet.")
        time.sleep(2)
        return
    
    while True:
    
        search_term = input("\nEnter a keyword, or press Enter to cancel: ").strip().lower()

        if search_term == "":
            return

        matching_notes = []

        for note in notes:
            if search_term in note.lower():
                matching_notes.append(note)

        if not matching_notes:
            print("\nNo matching notes found.")
        else:
            print("\n" + "=" * 15)
            print("Matching Notes:")
            print("=" * 15)
            display_notes(matching_notes)

        input("\nPress Enter to return to the Notes menu...")
        return