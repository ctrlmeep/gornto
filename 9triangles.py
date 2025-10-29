#Name: Benny Landon
#Due Date: 10/29/25
#Program Description: Asks for the side length of the triangles and the number of triangles and prints the number of triangles using asterisks.

sideLength = int(input("What is the side length of a triangle? ")) #input
triangles = int(input("How many triangles? "))
print()

for triangles in range(triangles):
    for rows in range(sideLength):
        for columns in range(rows + 1):
            print("* ", end = "")
        print()
    print()
