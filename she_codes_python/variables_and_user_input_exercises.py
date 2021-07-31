#Q1) Write a program that takes two numbers from theuser, and outputs their sum.

n1 = input("Hi! Please enter a number...")
n2 = input("Please enter another number...")
sum = float(n1) + float(n2)
print(f"{n1} + {n2} = {sum}")

#Q2) Write a program that takes two numbers from the user, and outputs the equation representing the multiplication of the two numbers.

n1 = input("Enter a number: ")
n2 = input("Enter another number: ")
result = float(n1) * float(n2)
print(f"{float(n1)} * {float(n2)} = {result}")

#Q3) Write a program that takes a distance in kilometers from the user, and outputs the distance in meters and centimeters.

km = input("How many kilometres?")
m = float(km) * 1000
cm = float(km) * 100000
print(f"{km}km = {int(m)}m")
print(f"{km}km = {int(cm)}cm")

#Q4) Write a program that takes the users name and height (in centimeters), and outputs a summary sentence. 

name = input("What is your name? ")
height = input("How tall are you (cms)? ")
print(f"{name} is {height}cms tall.")