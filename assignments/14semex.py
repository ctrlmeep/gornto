"""
Name: ************
Due Date: 12/11/25
Description: Determines what you grade will need to be on
the exam in order to get a desired letter grade and if you
will need extra credit to do that.

"""

#declares grades
grades = ["an A.", "a B.", "a C.", "a D."]
percentages = [89.5, 79.5, 69.5, 59.5]
choice = "yes"
guarFlag = False

print("***Semester Grade Calculator***\n")
while choice == "yes" or choice == "y":
    q1 = float(input("What is the quarter 1 grade: "))
    q2 = float(input("What is the quarter 2 grade: "))

    if q1 < 39:
        q1 = 39
    if q2 < 39:
        q2 = 39
    if q1 > 100:
        q1 = 100
    if q2 > 100:
        q2 = 100

    print("\nQuarter 1 Grade: " + str(q1) + "\tQuarter 2 Grade: " + str(q2))
    for i in range(len(grades)):
        exam = (percentages[i] / .2) - 2 * q1 - 2 * q2
        print("\nYou will need " + str(exam) + " to receive " + grades[i])
        if exam > 100:
            print("\tYou will need extra credit to get " + grades[i])
        if exam <= 0 and guarFlag == False:
            print("You are guaranteed to get " + grades[i])
            guarFlag = True
        print("________________________________________")

    choice = input("\nWould you like to calculate another grade? ").lower().strip()
    print()

print("Good Luck on your exams!")