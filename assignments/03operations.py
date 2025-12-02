#Name: ************
#Due Date: 10/01/25
#Program Description: Write an application that asks the user for the input of the user's name and then
#displays a greeting to the user.
#The application that asks the user for the input of 2 integer values.
#The application will calculate the sum, difference, product, quotient, and modulus
#of the two numbers and will display them as a math sentence to the screen on separate lines.
#Be sure to properly comment your code.

name = input("What is your name? ")
print("Greetings, " + name + "!")

first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))
print()

sum_result = str(first_number + second_number)
difference_result = str(first_number - second_number)
product_result = str(first_number * second_number)
quotient_result = str(first_number / second_number)
modulus_result = str(first_number % second_number)
first_number = str(first_number)
second_number = str(second_number)

print(first_number + " - " + second_number + " = " + difference_result)
print(first_number + " * " + second_number + " = " + product_result)
print(first_number + " / " + second_number + " = " + quotient_result)
print(first_number + " mod " + second_number + " = " + modulus_result)
print(first_number + " + " + second_number + " = " + sum_result)