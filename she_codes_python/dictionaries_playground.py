# students = ["Angela", "Jen", "Bel"]
# print(students[0])

# Creating a dictionary, separated with comma
# Elements are key: value pairs
# Keys need to be unique, keys can be only immutable
# Immutable data types -> String, Interger, Float, Bool, List
# Values don't need to be unique, any data type
# Dictionaties are unordered

# students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
# print(students_dict)

# print(students_dict["Angela"])

# students_dict["Asli"] = 4
# print(students_dict)
# students_dict["Jen"] = 10
# print(students_dict)

# del students_dict["Asli"]
# print(students_dict)

# print(students_dict.keys())
# print(students_dict.items())

# Iteration
# for key in students_dict:
#     print(key, students_dict[key])

# for key, value in students_dict.items():
#     print(key, value)

# print(students_dict.get("Bel"))
# print(students_dict.get("Asli", 0))  # If not found, return 0 or a string "Hello" for ex

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 0.56,
    "Oranges": 3.08
}

# print(groceries)

# looking at a specific value
# print(groceries["Baby Spinach"])

# adding a new item
# groceries["Avocadoes"] = 1.00
# print(groceries)

# # changing the value of an existing item
# groceries["Hot Chocolate"] = 2.70
# print(groceries)

# # removing an item from the dictionary
# del groceries["Crackers"]
# print(groceries)

# iterating over the dictionary
for item in groceries:
    print(f"{item}: ${groceries[item]}")

print()
   
# another way to iterate over the dictionary
for item, price in groceries.items():
    print(f"{item}: ${price}")