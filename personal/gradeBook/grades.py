import os
import json

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def export_json():
    filename = input("\nEnter filename (or press Enter for 'gradebook_export.json'): ").strip()
    if not filename:
        filename = "gradebook_export.json"
    elif not filename.endswith(".json"):
        filename += ".json"

    full_path = os.path.abspath(filename)
    print(f"\nFile will be saved to: {full_path}")

    confirm = input("\nIs this OK? (Y/n): ").strip().lower()
    if confirm == "y" or confirm == "":
        try:
            with open(filename, "w") as outputFile:
                json.dump(students, outputFile)
            print(f"\nSuccessfully exported to {full_path}")
        except Exception as e:
            print(f"\nError: {e}")
    else:
        print("\nExport cancelled.")

students = {}

def add_student(name):
    students[name] = {"grades" : []}

def add_grade(name, grade):
    try:
        students[name]["grades"].append(grade)
    except KeyError:
        print(f"\n{name} doesn't exist")

def get_average(name):
    grades = students[name]["grades"]
    try:
        return sum(grades) / len(grades)
    except KeyError:
        print(f"\n{name} doesn't exist")
    except ZeroDivisionError:
        return "No grades"

def display_all():
    if students == {}:
        print("No students in grade book yet.")
    for name in students:
        print(f"{name}: {', '.join(str(grade) for grade in students[name]["grades"])}")
    print()

def display_student(name):
    try:
        print(students[name]["grades"])
    except KeyError:
        print(f"\n{name} doesn't exist")


if __name__ == "__main__":
    try:
        with open("gradebook.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        with open("gradebook.json", "w") as file:
            json.dump(students, file)
    finally:
        with open("gradebookBackUp.json", "w") as file:
            json.dump(students, file)

    menuList = ["Add Student", "Add Grade", "Display Student's Grades", "Display Student's Grade Average", "Save Student's Grades", "Load Student's Grades (For debugging - Program automatically loads saved grades on start.)", "Clear/Delete Student's Grades", "Save and Exit", "Exit (Without Saving)", "Export"]
    while True:
        clear_screen()
        print()
        headerBorderWidth = int(40)
        print("=" * headerBorderWidth)
        print(" " * ((headerBorderWidth - 13) // 2) + "GRADE  TRACKER")
        print("=" * headerBorderWidth)
        display_all()
        print("-" * headerBorderWidth)
        print("\nWhat would you like to do?\n")
        for i in range(len(menuList)):
            print(str(i + 1) + ".\t" + menuList[i])
        print("-" * headerBorderWidth)
        choice = input("Enter your choice: ").strip()
        if choice == "1": add_student(input("\nEnter student name: "))
        if choice == "2": add_grade(input("\nEnter student name: "), int(input("\nEnter grade: ")))
        if choice == "3":
            display_student(input("\nEnter student name: "))
            input("\nPress Enter to continue...")
        if choice == "4":
            print(get_average(input("\nEnter student name: ")))
            input("\nPress Enter to continue...")
        if choice == "5":
            with open("gradebook.json", "w") as file:
                json.dump(students, file)
        if choice == "6":
            with open("gradebook.json", "r") as file:
                students = json.load(file)
        if choice == "7":
            with open("gradebook.json", "w") as file:
                students = {}
        if choice == "8":
            with open("gradebook.json", "w") as file:
                json.dump(students, file)
            break
        if choice == "9":
            break
        if choice == "10":
            print(f"\nCurrent directory: {os.getcwd()}")
            export_json()
        else:
            print("Invalid input, please enter a number 1-10.")
