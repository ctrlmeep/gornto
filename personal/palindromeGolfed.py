a=input("\nEnter the phrase: ")
b=a.lower().replace(" ","")
print(f"\n\"{a}\" is {"not "*(b!=b[::-1])}a palindrome!")