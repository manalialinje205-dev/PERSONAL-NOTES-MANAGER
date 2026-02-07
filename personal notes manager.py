import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    notes = load_notes()
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes(notes)
    print("Note added successfully!")


def view_notes():
    notes = load_notes()
    if not notes:
        print(" No notes found.")
        return

    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
        print("-" * 20)


def edit_note():
    notes = load_notes()
    note_id = int(input("Enter note ID to edit: "))

    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("New title: ")
            note["content"] = input("New content: ")
            save_notes(notes)
            print(" Note updated!")
            return

    print(" Note not found.")


def delete_note():
    notes = load_notes()
    note_id = int(input("Enter note ID to delete: "))

    new_notes = [note for note in notes if note["id"] != note_id]

    if len(notes) == len(new_notes):
        print(" Note not found.")
    else:
        save_notes(new_notes)
        print(" Note deleted!")


def menu():
    while True:
        print("\n--- Personal Notes Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
menu()

