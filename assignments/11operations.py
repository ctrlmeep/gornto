"""
Name: ************
Due Date: 11/13/25
Description:
Write a continuous-run (not one-and-done) program that has 5 procedures (functions, methods).
The program will input 2 integer values and then perform the five operations (+, -, x, ÷, mod)
in a mathematical statement.
    Continuous run
    Create 5 appropriately named functions that return the
     - Addition (2 input numbers)
     - Subtraction (2 input numbers)
     - Multiplication (2 input numbers)
     - Division (2 input numbers)
     - Mod (2 input numbers, this will not have a return statement)

"""
def add(a, b): #adding
    ans = round(a + b, 4)
    ans = str(a) + " + " + str(b) + " = " + str(ans)

    return ans

def subtract(a, b): #subtracting
    ans = round(a - b, 4)
    ans = str(a) + " - " + str(b) + " = " + str(ans)

    return ans

def multiply(a, b): #multiplication
    ans = round(a * b, 4)
    ans = str(a) + " * " + str(b) + " = " + str(ans)

    return ans
1
def divide(a, b): #division
    ans = round(a / b, 4)
    ans = str(a) + " / " + str(b) + " = " + str(ans)

    return ans

def modulus(a, b): #mod (no return, just print)
    ans = round(a % b, 4)
    print(str(a) + " mod " + str(b) + " = " + str(ans))
    
choice = "y"
while choice == "y":
    #inputs
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))

    #printing
    print()
    print(add(num1, num2))
    print(subtract(num1, num2))
    print(multiply(num1, num2))
    print(divide(num1, num2))
    modulus(num1, num2)

    #loop again (y/n)
    choice = input("\nWould you like to go again?(y/n) ")
    print()

print("The End!")
