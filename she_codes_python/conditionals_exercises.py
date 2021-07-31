#Q1) Kate’s cat, Roary, loves catching moths. Write a program that determines whether or not 
# it is time for Roary catch moths.

moths_in_house = True

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

#Q2) But Roary can’t actually get the moths by herself! 
# Amend the previous program to determine whether or not it is time for Roary to go moth hunting.

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")
else:
    print("No threats detected.")

#Q3) Write a program that implements the algorithmfor Red Light Cameras.

light_colour = "Red"
car_detected = True

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

#Q4) Write a program that asks the user for their height, and determines whether or not they are tall 
# enough to ride the rollercoaster, which has a height requirementof 120cms.

height = input("What is your height in cms? ")
height = float(height)

if height >= 120:
    print("Hop on!")
elif height < 120:
    print("Sorry, not today :(")

#Q5) Write a program that asks the user to enter their username and password, and outputs a success 
# message if they are correct, or a failure message if they are incorrect.

username = "fleur"
password = "password123"

input_username = input("Username: ")
input_password = input("Password: ")

if input_username == username and input_password == password:
    print("Correct!")
else:
    print("Incorrect!")

#Q6) Write a program that asks the user to enter their email address and checks whether it is valid or not. 
# For the purpose of this exercise, you can make the assumption that a valid email address contains 
# a “@” symbol and a “.” symbol.

email = input("Email: ")

if "@" in email and "." in email:
    print("Valid email address.")
else: 
    print("Invalid email adress.")






