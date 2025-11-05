import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print(f"{name}: ", end="")
        for grade in students[name]["grades"]:
            print(grade, end=", ")
        print()
    print()

def display_student(name):
    try:
        print(students[name]["grades"])
    except KeyError:
        print(f"\n{name} doesn't exist")


if __name__ == "__main__":
    while True:
        clear_screen()
        print()
        print("=" * 40)
        print("GRADE TRACKER")
        print("=" * 40)
        display_all()
        print("-" * 40)
        print("What would you like to do?")
        print("1. Add student")
        print("2. Add grade")
        print("3. Display Student's Grades")
        print("4. Display Student's Grade Average")
        print("5. Exit")
        print("-" * 40)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(input("\nEnter student name: "))
        if choice == "2":
            add_grade(input("\nEnter student name: "), int(input("\nEnter grade: ")))
        if choice == "3":
            display_student(input("\nEnter student name: "))
            input("Press Enter to continue...")  # Pause so user can see result
        if choice == "4":
            print(get_average(input("\nEnter student name: ")))
            input("Press Enter to continue...")  # Pause so user can see result
        if choice == "5":
            break

        input("\nPress Enter to continue...")