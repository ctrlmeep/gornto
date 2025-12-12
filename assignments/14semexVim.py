"""
Name: ************
Due Date: 12/11/25
Description: Calculates the grade required on your exam in order 
to get a desired semester grade.
Includes error proofing and indications of minimum letter grade 
and if extra credit is required.
"""

letterGrades = ["an A.", "a B.", "a C.", "a D."]
percentages = [89.5, 79.5, 69.5, 59.5]
choice = "yes"
guarFlag = False

print("***Semester Grade Calculator***\n")
while choice == "yes" or choice == "y":
	q1 = float(input("What is the quarter 1 grade: ").strip())
	q2 = float(input("What is the quarter 2 grade: ").strip())

	if q1 < 39: q1 = 39
	if q2 < 39: q2 = 39
	if q1 > 100: q1 = 100
	if q2 > 100: q2 = 100

	print(f"\nQuarter 1 Grade: {str(q1)}\tQuarter 2 Grade: {str(q2)}\n")
	for i in range(len(percentages)):
		exam = (percentages[i] / .2) - 2 * q1 - 2 * q2
		print(f"You will need {str(exam)} to receive {percentages[i]}")
		if exam > 100: print(f"\tYou will need extra credit to get {percentages[i]}")
		if exam <= 0 and guarFlag == False:
			print(f"You are guaranteed to get {percentages[i]}")
			guarFlag = True
		print("\n" + "-" * 30 + "\n")
	choice = input("\nWould you like to calculate another grade? ").lower().strip()
	print()

print("Good luck on your exams!") 
