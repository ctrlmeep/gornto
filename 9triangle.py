#Name: Benny Landon
#Due Date: 10/29/25
#Program Description: Asks for the side length of a triangle and prints a triangle using asterisks.

sideLength = int(input("What is the side length of a triangle? ")) #input
print()

for rows in range(sideLength):
    for columns in range(rows + 1):
        print("* ", end = "")
    print()
