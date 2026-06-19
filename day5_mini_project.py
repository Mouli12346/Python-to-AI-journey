import json
import os

def load_notes():
    if os.path.exists("my_notes.json"):
        with open("my_notes.json", "r") as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open("my_notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Load existing notes
notes = load_notes()
print(f"You have {len(notes)} saved notes")
print()

while True:
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        note = input("Write your note: ")
        notes.append(note)
        save_notes(notes)
        print("Note saved!")

    elif choice == "2":
        if len(notes) == 0:
            print("No notes yet")
        else:
            for i, note in enumerate(notes):
                print(f"{i+1}. {note}")

    elif choice == "3":
        print("Goodbye!")
        break

    print()