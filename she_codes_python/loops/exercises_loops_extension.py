# Q1) Below is a list of foods and their prices per unit:

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is providedin the same order as defined in the list above.

receipt = []
total_cost = 0

# For each item in the list of groceries...
for item in groceries:
    # Ask the user for the number of units they bought
    units = input(f'How many units of {item[0]} did you buy? ')
    # Calculate the cost by multiplying the item's price by the number of units bought
    item_cost = item[1] * float(units)
    # Increment the total cost by the new item cost
    total_cost += item_cost
    # Create the new receipt line item
    receipt.append(f'{item[0]} ${item_cost:.2f}')

print("====Izzy's Food Emporium====")

for line in receipt:
    print(line)

print("============================")
print(f'${total_cost:.2f}')

# Q2) Ask the user to enter a string. Output the string one character at a time, 
# as well as it’s position in the string.

string = input("Please enter a string: ")
number = 0

for letter in string:
    print(number, letter)
    number += 1

# Q3) Ask the user for a number and use this to generate a pyramid of that height.

height = int(input("Pyramid size: "))

for number in range(height + 1):
    for i in range(number + 1):
        print("*", end="")
    print("")

# Q4) Ask the user for a number and use this to generate a (different) pyramid of that height.

rows = int(input("Pyramid size: "))
row = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):    #rows = the total number of rows and i = the current row number.
        print(end="  ")
   
    while row != ((2 * i) - 1):
        print("* ", end="")
        row += 1
   
    row = 0
    print()