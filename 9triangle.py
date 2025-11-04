#Name: ************
#Due Date: 10/29/25
#Program Description: Asks for the side length of a triangle and prints a triangle using asterisks.

sideLength = int(input("What is the side length of a triangle? ")) #input
print()

for rows in range(sideLength, 0, -1): #printing
    for columns in range(rows, 0, -1):
        print("* ", end = "")
    print()
