# Q1) Given the list of foods below, output:

foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]

# 1. The first item in the list.
print(foods[0])

# 2. The third item in the list.
print(foods[2])

# 3. The last item in the list.
print(foods[-1])

# 4. The first three items in the list.
print(foods[0:3])

# 5. The last three items in the list.
print(foods[-3:])

# # 6. The last item in the sublist
print(foods[6][-1])

#Q2) Format and print the following list:

# mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]
print(mailing_list[0][0] + ": " + mailing_list[0][1])
print(mailing_list[1][0] + ": " + mailing_list[1][1])
print(mailing_list[2][0] + ": " + mailing_list[2][1])
print(mailing_list[3][0] + ": " + mailing_list[3][1])
print(mailing_list[4][0] + ": " + mailing_list[4][1])

#Q3) Ask the user for three names, add them to a list, then print the list.

name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")

names = []
names.append(name1)
names.append(name2)
names.append(name3)

print(names)

# Q4) Using the following starter code:

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# Produce the following lists:

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d.insert(0, a)
d.insert(1, b)
d.insert(2, c)
print(d)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
abc = a + b + c
print(abc)