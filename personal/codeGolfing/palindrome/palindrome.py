#program that detects if a word or phrase is a palindrome

rawPhrase = input("\nEnter the phrase: ")
phrase = rawPhrase.lower().replace(" ", "")

if phrase == phrase[::-1]: print(f"\n\"{rawPhrase}\" is a palindrome!")
else: print(f"\n\"{rawPhrase}\" is not a palindrome!")