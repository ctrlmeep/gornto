# Below is some python code for a madlib program.
# You are to cnp this code into a new program. (madlib 10.py)
# Create the 8 appropriately named lists (look in the code for the proper name of the list).
# Each List will have a minimum of 5 elements, 
# that will randomly assign an element to the part of the story.  
# The program should not allow a word to be repeated.  
# See the sample output from class.
# Only one portion of the code below should be changed and you will see it "<here>"

#working section

#APIs
import random

#lists
adj = ["funny", "big", "small", "loud", "quiet", "red", "green", "blue", "black", "white"]
noun = ["car", "cat", "dog", "ball", "shoe", "plane", "house"]
pluralNoun = ["toys", "apples", "bananas", "socks", "pencils"]
game = ["Chess", "Tic-Tac-Toe", "Rock-Paper-Scissors", "I-Spy", "Hop-Scotch"]
ingVerb = ["running", "playing", "reading", "dancing", "jumping"]
plant = ["grass", "shrub", "tree", "vine", "moss"]
bodyPart = ["foot", "face", "hand", "arm", "leg"]
place = ["Melbourne High School", "Mr. Gornto's house", "McDonald's", "The Melbourne Causeway", "Palm Bay High School"]

adj1 = random.choice(adj)
adj.remove(adj1)

adj2 = random.choice(adj)
adj.remove(adj2)

noun2 = random.choice(noun)
noun.remove(noun2)

noun3 = random.choice(noun)
noun.remove(noun3)

pluralNoun1 = random.choice(pluralNoun)
pluralNoun.remove(pluralNoun1)

game1 = random.choice(game)
game.remove(game1)

pluralNoun2 = random.choice(pluralNoun)
pluralNoun.remove(pluralNoun2)

ingVerb1 = random.choice(ingVerb)
ingVerb.remove(ingVerb1)

ingVerb2 = random.choice(ingVerb)
ingVerb.remove(ingVerb2)

pluralNoun3 = random.choice(pluralNoun)
pluralNoun.remove(pluralNoun3)

ingVerb3 = random.choice(ingVerb)
ingVerb.remove(ingVerb3)

noun4 = random.choice(noun)
noun.remove(noun4)

plant1 = random.choice(plant)
plant.remove(plant1)

bodyPart1 = random.choice(bodyPart)
bodyPart.remove(bodyPart1)

place1 = random.choice(place)
place.remove(place1)

ingVerb4 = random.choice(ingVerb)
ingVerb.remove(ingVerb4)

adj3 = random.choice(adj)
adj.remove(adj3)

pluralNoun4 = random.choice(pluralNoun)
pluralNoun.remove(pluralNoun4)

hours = str(random.randint(2, 24))

#printing section
print()
print("-------------My Mad Lib-------------")
print()
print("A vacation is when you take a trip to some " + adj1 +" place")
print("with your " + adj2 + " family. Usually you go to some place ")
print("that is near a/an " +noun2 +" or up on a/an "+ noun3)
print("A good vacation place is one where you can ride " + pluralNoun1)
print("or play " + game1 +" or go hunting for " + pluralNoun2 + ".  I like ")
print("to spend my time " + ingVerb1 + " or "+ingVerb2 + ".")
print("When parents go on a vacation, they spend their time eating")
print("three " + pluralNoun3 +" a day, and fathers play golf, and mothers ")
print("sit around " + ingVerb3 + ". Last summer, my little brother ")
print("fell in a/an " + noun4 + " and got poison " + plant1 + " all")
print("over his " + bodyPart1 + ".  My family is going to go to (the) ")
print(place1 + " , and I will practice "+ingVerb4+".  Parents")
print("need vacations more than kids because parents are always very ")
print(adj3+" and because they have to work ", hours) #insert a random integer generator for the appropriate number here
print("hours every day all year making enough " + pluralNoun4 + " to pay " )
print("for the vacation.")

##print(adj1)
##print(adj2)
##print(adj3)
##
##print(noun2)
##print(noun3)
##print(noun4)
##
##print(pluralNoun1)
##print(pluralNoun2)
##print(pluralNoun3)
##print(pluralNoun4)
##
##print(ingVerb1)
##print(ingVerb2)
##print(ingVerb3)
##print(ingVerb4)
##
##print(plant1)
##print(bodyPart1)
##print(place1)
##print(game1)
