#simple 4 function calculator (additionally with exponentiation, root, and modulus)
#with checks for dividing by zero and for improper inputs
import random

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("\n Error: Please enter a valid number!")

def get_operation():
    print("\nWhat operation would you like to perform?")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("^ : Exponentiation")
    print("r : Root")
    print("% : Modulus")
    print("! : Factorial")
    operation = input("\nEnter the operation symbol (+, -, *, /, ^, r, %, !): ").strip()

    if operation == "I'm feeling lucky!":
        operation = random.choice(['+', '-', '*', '/', '^', 'r', '%', '!'])
        print("\nYou said you were feeling lucky! So you were given a random operation!\n\nYour operation is:", operation)

    return operation

def compute():
    while True:
        first_number = get_valid_number("\nWhat is the first number? ")
        operation = get_operation()
        if operation ==  "!":
            if first_number % 1 == 0:
                if first_number < 0:
                    print("\nError: Factorial is not defined for negative numbers.")
                    continue
                elif first_number == 0:
                    result = 1
                else:
                    factorial_result = 1
                    for i in range(1, int(first_number) + 1):
                        factorial_result *= i
                    result = factorial_result
                print(f"\nAnswer: {result}")
                break
            else:
                print("\nError: Factorial is not defined for fractions.")
                continue

        second_number = get_valid_number("\nWhat is the second number? ")

        if operation == "+":
            print(f"\nAnswer: {first_number + second_number}")
            break
        elif operation == "-":
            print(f"\nAnswer: {first_number - second_number}")
            break
        elif operation == "*":
            print(f"\nAnswer: {first_number * second_number}")
            break
        elif operation == "/":
            if second_number == 0: print("\nError: Cannot divide by zero!")
            else:
                print(f"\nAnswer: {first_number / second_number}")
                break
        elif operation == "^":
            print(f"\nAnswer: {first_number ** second_number}")
            break
        elif operation == "r":
            if second_number <= 0: print("\nError: Cannot divide by zero!")
            else:
                print(f"\nAnswer: {first_number ** (1 / second_number)}")
                break
        elif operation == "%":
            if second_number == 0: print("\nError: Cannot divide by zero!")
            else:
                print(f"\nAnswer: {first_number % second_number}")
                break
        else: print("\nInvalid operation! Please use +, -, *, /, ^, r, %, !.")
        break

def main():
    print("Calculator")
    print("----------")
    while True:
        compute()
        if input("\nPress ENTER to continue or type 'quit' to exit: ").lower() == "quit":
            break

if __name__ == "__main__":
    main()
