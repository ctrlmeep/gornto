import os

commandCatalog = {
    "rm": "Delete a file. Usage: rm <filename>",
    "mk": "Create a new file. Usage: mk <filename>",
    "open": "Open a file in nano editor. Usage: nano <filename>",
    "cd": "Change directory. Usage: goto <directory_path>",
    "mkdir": "Create a new directory. Usage: mkdir <directory_name>"
}

def command_separation(command):
    """Separate the command from its arguments."""
    parts = command.strip().split(" ", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    else:
        return parts[0], ""

def command_search(command):
    """Search for a command in the command catalog."""
    cmd, args = command_separation(command)
    if cmd in commandCatalog:
        if args != "":
            if cmd == "mk":
                mk(args)
            if cmd == "open":
                open_file(args)
            if cmd == "rm":
                rm(args)
            if cmd == "cd":
                cd(args)
            if cmd == "mkdir":
                mkdir(args)
        else:
            print(f"\n{cmd}: {commandCatalog[cmd]}")

def mk(command):
    """Create a new file specified in the command."""
    command_separation(command)
    with open(command, "w"):
        pass
    print(f"\nCreated file: {command}")

def open_file(command):
    """Open a file in nano editor specified in the command."""
    command_separation(command)
    print("\nEnter text to append (or type 'exit' to quit): ")
    with open(command, "r") as file:
        content = file.read()
        print(f"\nContent of {command}:\n")
        print(content)
        print("--- Start Editing ---")
    while True:
        edit = input()
        if edit.lower() == "exit":
            break
        with open(command, "a") as file:
            file.write(edit + "\n")

def rm(command):
    """Delete a file specified in the command."""
    command_separation(command)
    os.remove(command)
    print(f"\nDeleted file: {command}")

def cd(command):
    """Change directory to the path specified in the command."""
    command_separation(command)
    os.chdir(command)
    print(f"\nChanged directory to: {os.getcwd()}")

def mkdir(command):
    """Create a new directory specified in the command."""
    command_separation(command)
    os.mkdir(command)
    print(f"\nCreated directory: {command}")

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_files():
    """Print all files in the current directory."""
    print("\nCurrent Directory: " + os.getcwd())
    print("\nFiles in current directory:")
    for file in os.listdir():
        print(file)

def help():
    """Display help information."""
    print("\nAvailable Commands:")
    for cmd in commandCatalog:
        print(f"{cmd}: {commandCatalog[cmd]}")

if __name__ == "__main__":
    while True:
        clear_screen()
        print_files()
        command = input("\nEnter a command ('help' for help and 'exit' to quit): ").strip()
        if command.lower() == "exit":
            break
        command_search(command)

