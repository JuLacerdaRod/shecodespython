#Variables
#String str
dog = "Jett"
print(dog)
print(type(dog))

asli = f"Hey, my dog's name is {dog}"
print(asli)

day = "Saturday"
print(type(day))

message = f"Today is {day}!"
print(message)

month = "November"
message2 = f"Today is {day} and we are in {month}!"
print(message2)

# Integer (without decimals)
# Float (with decimals)

apples = 5
banana = 8
fruits = apples + banana
print(fruits)
print(type(fruits))

height = 1.70
weight = 999.9
calculation = weight - height
print(calculation)
print(type(calculation))

calculation = height + banana
print(calculation)   

# Integers
# Run distance in m
run1_dist = 1400
run2_dist = 1800

# Addition
total_distance = run1_dist + run2_dist
print(total_distance)

# Floats
# Run distance in km
run3_dist = 1.7
run4_dist = 1.35

# Addition
total_distance = run3_dist + run4_dist
print(total_distance)

# Division and Multiplication
example_distance = run1_dist / run2_dist
print(run1_dist / 1000)
print(run4_dist * 1000)

goal_dist = 8000
run1_left = 0
print(run1_dist)

run5_dist = "5000"

print(run5_dist + 3)  # error
print(run5_dist + "3")
print(run5_dist * 3)
print(run5_dist * 3.0)  # error

# Typecasting
print(int(run5_dist) + 3)
print(str(3))