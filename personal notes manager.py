import json
import os

FILE_NAME = "notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    notes = load_notes()
    new_id = max([n['id'] for n in notes], default=0) + 1
    
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    
    notes.append({"id": new_id, "title": title, "content": content})
    save_notes(notes)
    print(f"Note #{new_id} added successfully!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("\n No notes found.")
        return

    print("\n--- Your Notes ---")
    for note in notes:
        print(f"[{note['id']}] {note['title']}\n    {note['content']}")
    print("-" * 20)

def edit_note():
    notes = load_notes()
    try:
        note_id = int(input("Enter note ID to edit: "))
    except ValueError:
        print("Please enter a valid numerical ID.")
        return
        
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input(f"New title ({note['title']}): ") or note['title']
            note["content"] = input(f"New content: ") or note['content']
            save_notes(notes)
            print("Note updated!")
            return
    print("Note not found.")

def delete_note():
    notes = load_notes()
    try:
        note_id = int(input("Enter note ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    filtered_notes = [n for n in notes if n["id"] != note_id]

    if len(notes) == len(filtered_notes):
        print("Note not found.")
    else:
        save_notes(filtered_notes)
        print("Note deleted!")

def menu():
  actions = {
        "1": add_note,
        "2": view_notes,
        "3": edit_note,
        "4": delete_note
    }   
    while True:
        print("\n--- Personal Notes Manager ---")
        print("1. Add  2. View  3. Edit  4. Delete  5. Exit")
        choice = input("Select: ")

        if choice == "5":
            print("Goodbye!")
            break
            
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()

                                                


