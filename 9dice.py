#Name: ************
#Due Date: 11/4/25
#Program Description: Write a python program that will simulate a pair of 6 sided dice being rolled. The user will determine how many rolls are necessary.
#Input will be how many times the user wishes to roll. Output will be the roll number, the roll of each die and comment (below)

#If the dice rolled are both:
#1  “Snake Eyes”
#2  “Ballerina”
#3  “Brooklyn Forest”
#4  “Square Pair”
#5  “Puppy Toes”
#6  “Boxcars”

#After the program has run, it will display the number of each and the percentage of each.
#See the sample output in class.

import random

rolls = input("How many rolls would you like? ")

print("\nRolls\tDie1\tDie2\tComments")
print("-----\t----\t----\t--------")

snakeEyes = 0
ballerina = 0
brooklynForest = 0
squarePair = 0
puppyToes = 0
boxCars = 0

for i in range(int(rolls)):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    comment = ""
    if roll1 == roll2:
        if roll1 == 1:
            comment = "Snake Eyes"
            snakeEyes += 1
        if roll1 == 2:
            comment = "Ballerina"
            ballerina += 1
        if roll1 == 3:
            comment = "Brooklyn Forest"
            brooklynForest += 1
        if roll1 == 4:
            comment = "Square Pair"
            squarePair += 1
        if roll1 == 5:
            comment = "Puppy Toes"
            puppyToes += 1
        if roll1 == 6:
            comment = "Box Cars"
            boxCars += 1

    print(str((i + 1)) + "\t" + str(roll1) + "\t" + str(roll2) + "\t" + comment)

print("\nThe number of Snake Eyes: " + str(snakeEyes) + "\t\tPercent of Snake Eyes: " + str(round(snakeEyes / int(rolls) * 100, 1)))
print("The number of Ballerina: " + str(ballerina) + "\t\tPercent of Ballerina: " + str(round(ballerina / int(rolls) * 100, 1)))
print("The number of Brooklyn Forest: " + str(brooklynForest) + "\tPercent of Brooklyn Forest: " + str(round(brooklynForest / int(rolls) * 100, 1)))
print("The number of Square Pair: " + str(squarePair) + "\t\tPercent of Square Pair: " + str(round(squarePair / int(rolls) * 100, 1)))
print("The number of Puppy Toes: " + str(puppyToes) + "\t\tPercent of Puppy Toes: " + str(round(puppyToes / int(rolls) * 100, 1)))
print("The number of Box Cars: " + str(boxCars) + "\t\tPercent of Box Cars: " + str(round(boxCars / int(rolls) * 100, 1)))

