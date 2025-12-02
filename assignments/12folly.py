#Name: ############
#Due Date: 12/3/25
#Program Description:


import random

#header printing
print("*** Welcome to Lucky Seven Dice Game! ***")
print("If the sum of the Dice is 7, you win $4. Otherwise, you lose $1.")

#variable declaration
total = int(input("\nHow many dollars do you have? "))
rolls = 0
highestTotal = total
highestRoll = rolls

#chart header printing
print("\nRoll:\tDie 1:\tDie 2:\tSum:\tBalance:")
print("-------\t-------\t-------\t-------\t-------")

#chart printing and logic
while total > 0:
    rolls += 1
    die1 = random.randint(1, 7)
    die2 = random.randint(1, 7)
    if die1 + die2 == 7:
        total += 4
    else:
        total -= 1

    if total > highestTotal:
        highestTotal = total
        highestRoll = rolls

    #chart line printing
    print(str(rolls) + "\t" + str(die1) + "\t" + str(die2) + "\t" + str(die1 + die2) + "\t" + str(total))

#footer printing
print("You are broke after " + str(rolls) + " rolls.")
print("You should have quit after " + str(highestRoll) + " rolls when you had $" + str(highestTotal) + ".")



