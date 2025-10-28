#Name: B**** L*****
#Due Date: 10/28/25
#Program Description: Create an application named StringMisc8 that reads in a string from the user.
#Outputs:
#the string
#length of string
#the string reversed (using methods discussed in class)
#the 3rd-7th  characters displayed

userInput = input("Please enter a string: ") #string input

print("\nString: " + userInput) #reprinting string

print("Length of String: " + str(len(userInput))) #printing length of string

print("The String reversed: ", end="") #printing string reversed
for n in range(len(userInput), 0, -1):
    print(userInput[n -1], end="")
print()

print("The 3rd through 7th characters are: " + (userInput[2:7])) #printing string's characters 3-7
