#Loops - repetitive tasks

for number in range(10): #iterate through sequence of numbers
    print(number)

for num in range(5):
    print(num)

for num in range(1,11,2):
    print(num)

# Use for loop to print numbers 0 to 100 (inclusive)

for num in range(101):
    print(num)

#Use for loop to print numbers 0 to 100 (skip 5)

for num in range(0, 100, 5):
    print(num)

letters = ["a", "b", "c", "d"]
result = ""

for letter in letters:
    result = result + letter
    print(result)  #print every step
print(result)      #print final result

chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

for item in range(len(chilli_wishlist)):  # range(4)
    print(chilli_wishlist[item])

for item in chilli_wishlist:
    print(item)

# Adapt the foor loop to print a message
# for each item in the list eg "Chilli wants: "

for item in chilli_wishlist:
    print(f"Chilli wants: {item}")
    # print("Chilli wants " + chilli_wishlist[item])  # TypeError

# Use a for loop to print each item in a list 
# from a previous exercise or example

for letter in letters:
    print(letter)

numbers = [[1, 2, 3],[4],[5, 6]]

print(numbers[2] [-1])

for number in numbers:
    for digit in number:
        print(digit)

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "kong", "dig mat"]
]

for category in chilli_wishlist:
    for item in category:
        print(item)

# While loops

guess = ""
while guess != "a":
    guess = input("Guess a letter: ")


counter = 0

while counter <= 10:
    print(counter)
    counter = counter + 1


count = 0

while count < 5:
    print("Hello")
    #count = count + 1
    count += 1