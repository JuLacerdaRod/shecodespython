# Q1)The dictionary below represents the cost of individual items in a supermarket. A separate dictionary is given in the table below,
# this dictionary represents the quantity of each item purchased. Use these two dictionaries to write a program that outputs the cost of each item.
# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }

# for item in groceries:
#     print(f"{quantity[item]} {item} @ ${groceries[item] = quantity[item] * groceries[item] * groceries[item]:.2f}")


#Q2)

# colour_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
# }

# for colour in colours:
#     colour_counts[colour] += 1

# print(colour_counts)

#Q3)

# names = [
# "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
# "Joy", "Katie", "Maddie", "Tash", "Nic",
# "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
# "Viv", "Anna", "Catherine", "Catherine", "Debby",
# "Gab", "Megan", "Michelle", "Nic", "Roxy",
# "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

# list_names = list(set(names))

# names_dict = {}.fromkeys(names, 0)

# for name in names:
#     names_dict[name] += 1

# print(names_dict)

#Q4) 

import csv

colour_dict = {}

with open("starter2/colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for line in csv_reader:
        colour_dict[line[1]] = line[2]

# print(f" {line[1]} {line[2]}")

print(colour_dict)


# Q5)

import csv

colour_dict = {}

with open("starter2/colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for line in csv_reader:
        colour_dict[line[1]] = [line[0], line[2]]

# print(f" {line[1]} {line[2]}")

print(colour_dict)