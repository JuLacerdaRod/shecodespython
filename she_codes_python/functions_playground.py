#Create function that takes in an integer as a parameter and returns that integer multiplied by 3

# def calc(input_number):
#     input_number = input("Enter a number: ")
#     number = int(input_number) * 3
#     return number

# print(calc)

# examples

# def convert_cm_to_in(length_cm):
#     length_in_inch = length_cm / 2.54
#     return length_in_inch

# print(convert_cm_to_in(20))
# print(length_in_inch) #is not defined, local var


#Write a function that converts inches to centimeters

# def convert_in_to_cm(lenght_in_inch):
#     lenght_in_cm = lenght_in_inch * 10
#     return lenght_in_cm

# print(convert_in_to_cm(50))

# Calculate the mean of two numbers:

def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(3,4))
