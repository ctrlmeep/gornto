#Name: ************
#Due Date: 10/29/25
#Program Description: Asks for the side length of a triangle and prints 4 triangles in different orientations using asterisks

sideLength = int(input("What is the side length of a triangle? ")) #input
print()

for n in range(0, sideLength):
    for m in range(0, n + 1):
        print("* ", end = "")
    print()
print()

for n in range(sideLength, 0, -1):
    for m in range(n, 0, -1):
        print("* ", end = "")
    print()
print()

for n in range(0, sideLength):
    for m in range((sideLength - n - 1), 0, -1):
        print("  ", end = "")
    for m in range(0, n + 1):
        print("* ", end = "")
    print()
print()

for n in range(0, sideLength):
    for m in range(0, n):
        print("  ", end = "")
    for m in range((sideLength - n), 0, -1):
        print("* ", end = "")
    print()

# Alternate Method (Not talked about in class yet)

#for n in range(0, sideLength):
#    print("  " * (sideLength - n - 1) + "* " * (n + 1))
#print()
#
#for n in range(sideLength, 0 , -1):
#    print("  " * (sideLength - n) + "* " * n)
#print()