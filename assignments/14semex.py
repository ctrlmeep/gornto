"""
Name: ************
Due Date: 12/9/25
Description: Determines what you grade will need to be on
the exam in order to get a desired letter grade and if you
will need extra credit to do that.

"""

#declares grades
grades = ["an A.", "a B.", "a C.", "a D."]
percentages = [89.5, 79.5, 69.5, 59.5]
choice = "yes"

while choice.lower() == "yes" or choice.lower() == "y":
    #gets quarter grades
    q1 = float(input("What is the quarter 1 grade: "))
    q2 = float(input("What is the quarter 2 grade: "))

    #Calculates needed grades and prints
    for i in range(len(grades)):
        exam = (percentages[i]/.2)-2*q1-2*q2
        print("\nYou will need " + str(exam) + " to receive " + grades[i])
        if exam > 100:
            print("\tYou will need extra credit to get " + grades[i])

    choice = input("\nDo you wish to continue? (yes/no): ")