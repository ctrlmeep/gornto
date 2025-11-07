import clearScreen
import os

files = []

def export_txt():
    filename = input("\nEnter filename: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    full_path = os.path.abspath(filename)
    print(f"\nFile will be saved to: {full_path}")

    confirm = input("\nIs this OK? (Y/n): ").strip().lower()
    if confirm == "y" or confirm == "":
        try:
            with open(filename, "w") as outputFile:
                outputFile.write("\n".join(files))
            print(f"\nSuccessfully exported to {full_path}")
        except Exception as e:
            print(f"\nError: {e}")
    else:
        print("\nExport cancelled.")

def validate_name(name):
    if not name[-4:] == ".txt":
        name += ".txt"
    return name

def new_note(name):
    name = validate_name(name)
    with open(name, "w") as file:
        file.write("")
    files.append(name)

def open_note(name):
    clearScreen.clear_screen()
    name = validate_name(name)
    with open(name, "r+") as file:
        print("Enter <Quit> to save and quit, otherwise, any text you enter will be stored.\n")
        print(file.read())
        while True:
            content = input()
            if content.lower().strip() == "quit":
                break
            else:
                file.write(content + "\n")

def delete_note(name):
    name = validate_name(name)
    os.remove(name)
    files.remove(name)

def delete_note_command(command):
    if command[:3] == "rm ":
        name = command[3:]
        delete_note(name)

def print_files():
    for file in files:
        print(file)

def load_files():
    for file in os.listdir():
        if file.endswith(".txt"):
            files.append(file)

if __name__ == "__main__":

    if not os.getcwd().endswith(os.sep + "notesFolder"):
        if not os.path.isdir("notesFolder"):
            os.mkdir("notesFolder")
        if os.path.isdir("notesFolder"):
            os.chdir("notesFolder")
    load_files()

    while True:
        clearScreen.clear_screen()
        print("\nWelcome to Personal Notes!\n")
        print("--------------------------")
        print("Files:")
        print_files()
        print("--------------------------")
        print("What would you like to do?")
        print("1 - Add new note")
        print("2 - Open note")
        print("3 - Delete note")
        print("4 - Exit")
        choice = input("\nEnter your choice: ").strip()

        try:
            if int(choice) == 1:
                new_note(name = input("\nWhat would you like to name the note? "))
            if int(choice) == 2:
                open_note(name = input("\nWhat note would you like to open? "))
            if int(choice) == 3:
                delete_note(name = input("\nWhat note would you like to delete? "))
            if int(choice) == 4:
                break
        except ValueError:
            try:
                if choice[:3] == "rm ":
                    delete_note(choice) # command system
            except Exception(BaseException):
                print("\nInvalid choice. Please try again.")
                input("\nPress Enter to continue...")