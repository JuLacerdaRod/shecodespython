# Boolean values

is_raining = False
is_cold = True

print(is_raining)
print(type(is_raining))
print(is_cold)
print(type(is_cold))

is_sunny = False
have_shoes = True
is_gym_open = True

print(is_sunny and have_shoes)
print(is_sunny or is_gym_open)

print(is_raining)
print(not is_raining)
print(is_raining and is_cold)
print(is_raining and not is_cold)

print(is_raining) #F
print(not is_raining) #T
print(is_raining or is_cold) #F or T = True
print(is_raining and not is_cold) #F and F = False
print(is_raining or not is_cold) #F or F = False
print(not is_raining and not is_cold) #T and F = False

print(5 < 3)
print(5 > 3)
print(10>= 10)
print(4 <= 10)
print(5 == 5)
print(5 != 4)

print(5.1 > 2.4)
print("Asli" == "asli")

temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print(temperature - wind_chill < 16)

name = "Hayley"
print(name == "Hayley")
print(name != "Hayley")

print("A" > "a")

# #syntax / semantics
var1 = 5

if var1 > 3:
    print("hello")

## if statements
is_raining = False

# if
if is_raining:
    print("Take an umbrella.")

# if and else
if is_raining:
    print("Take an umbrella.")
else:
    print("Do not take an umbrella.")

# if, elif, else
if temperature - wind_chill < 16:
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("Euck, it's hot today, stay home.")
else:
    print("Wow, what a lovely day!")   

#nested if statements
if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
            print("You'll need a jumper today.")

if temperature - wind_chill < 5 and is_raining:
    print("You'll need an umbrella today.")
if temperature - wind_chill < 16:
    print("You")




