#Name: Benny Landon
#Due Date: 10/29/25
#Program Description: Asks for the side length of a triangle and prints 4 triangles in different orentations using asterisks

sideLength = int(input("What is the side length of a triangle? ")) #input
print()

for rows in range(0, sideLength): 
    for columns in range(0, rows + 1):
        print("* ", end = "")
    print()
print()

for rows in range(sideLength, 0, -1): 
    for columns in range(rows, 0, -1):
        print("* ", end = "")
    print()
print()

for rows in range(0, sideLength):
    print("  " * (sideLength - rows - 1) + "* " * (rows + 1))
print()

for rows in range(sideLength, 0 , -1):
    print("  " * (sideLength - rows) + "* " * (rows))
print()

for rows in range(0, sideLength):
    for columns in range(0, rows + 1):
        print(" -", end = "")
    for columns in range(rows + 1, 0 , -1):
        print(" *", end = "")
    print()
