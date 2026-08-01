from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
NOTES_FILE = BASE_DIR / "notes.txt"

def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

    except FileNotFoundError:
        return []

    clean_notes = []

    for note in notes:
        clean_notes.append(note.strip())

    return clean_notes

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")