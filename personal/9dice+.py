import random

rolls = input("How many rolls would you like? ")
sides = int(input("How many sides are on the dice? "))

print("\nRolls\tDie1\tDie2\tComments")
print("-----\t----\t----\t--------")

pairs_data = {
    1: {"name": "Snake Eyes", "count": 0, "indents": 3},
    2: {"name": "Ballerina", "count": 0, "indents": 3},
    3: {"name": "Brooklyn Forest", "count": 0, "indents": 1},
    4: {"name": "Square Pair", "count": 0, "indents": 2},
    5: {"name": "Puppy Toes", "count": 0, "indents": 3},
    6: {"name": "Box Cars", "count": 0, "indents": 3}
}

for i in range(int(rolls)):
    roll1 = random.randint(1, sides)
    roll2 = random.randint(1, sides)
    comment = ""

    if roll1 == roll2:
        if roll1 <= 6:
            comment = pairs_data[roll1]["name"]
            pairs_data[roll1]["count"] += 1
        else:
            comment = ""

    print(f"{i + 1}\t{roll1}\t{roll2}\t{comment}")

print()

for die_value in range(1, 7):
    count = pairs_data[die_value]["count"]
    name = pairs_data[die_value]["name"]
    indents = pairs_data[die_value]["indents"]
    percent = round(count / int(rolls) * 100, 1)
    print(f"The number of {name}: {count}" + "\t" * indents + f"Percent of {name}: {percent}")