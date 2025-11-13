"""
Data Structure Cheat Sheet:
- List: [] , ordered, mutable, allows duplicates
- Tuple: (), ordered, immutable, allows duplicates
- Set: {} or set(), unordered, mutable, no duplicates
- Dict: {key:value}, ordered*, mutable, no duplicate keys
"""
#Mutable - can be changed
#Immutable - cannot be changed

list1 = ["Computer", "Printer", "TV", "Camera", 89, 30.8] #mutable
list1[0] = "PC" #changes first item
print(list1)

tuple1 = ("Computer", "Printer", "TV", "Camera", 89, 30.8) #immutable
#tuple1[0] = "PC" #will cause an error, can't be changed
print(tuple1)

set1 = set(["Computer", "Printer", "TV", "Camera", 89, 30.8]) #set keyword
print(set1)
set1 = {"Computer", "Printer", "TV", "Camera", 89, 30.8} #curly braces
print(set1)

set1.add("Laptop") #adds item to set
print(set1)
set1.remove("Laptop") #removes item from set
print(set1)

#Dictionary keys are immutable, values can be mutable or immutable
dictionary1 = { #word:definition
    "item1": "Computer",
    "item2": "Printer",
    "item3": "TV",
    "item4": "Camera",
    "item5": 89,
    "item6": 30.8
    } #key:value pairs in curly braces
print(dictionary1) #entire dictionary
print(dictionary1["item1"]) #access value by key

# Demonstrate mutability
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
print(f"list1: {list1}")  # [99, 2, 3] - list1 changed too!

# Demonstrate immutability
tuple1 = (1, 2, 3)
tuple2 = tuple1
# tuple2[0] = 99 would error - tuples can't be changed

# Sets automatically remove duplicates
set_with_dupes = {1, 2, 2, 3, 3, 3}
print(set_with_dupes)  # {1, 2, 3}

dictionary1["item7"] = "Laptop"  # Add new key-value pair
del dictionary1["item1"]  # Remove key-value pair
print("item2" in dictionary1)  # Check if key exists (True)

# List - for collections that might change
shopping_list = ["milk", "eggs", "bread"]
shopping_list.append("butter")  # Expected to change

# Tuple - for fixed collections
coordinates = (40.7128, -74.0060)  # Latitude, longitude - shouldn't change
rgb_red = (255, 0, 0)  # Color values - fixed definition