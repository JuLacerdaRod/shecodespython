import csv

# Q1) Write a program that reads in colours_20_simple.csv and output the colour data.

# import csv

# with open('starter/colours_20_simple.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(f'{row[0]} {row[1]} {row[2]}')

# Q2) Write a program that reads in colours_20_simple.csv and outputs the colour data in order English, Hex
# then RGB.

# import csv

# with open('starter/colours_20_simple.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for row in csv_reader:
#         print(f"{row[2]}, Hex: {row[1]}, RGB: {row[0]}")

# Q3) Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB.

# import csv

# with open('starter/colours_20.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for row in csv_reader:
#         print(f"{row[4]}, Hex: {row[2]}, RGB: {row[1]}")

# Q4) Using the same colour csv files, write a program that outputs the number of times each of the following
# colours appear in the English Name:
# ● red
# ● green
# ● blue

with open('starter/colours_20.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line  in csv_reader:
        print(line)


# Q5) galaxies.py contains data about 82 different galaxies and their velocities (km/sec). Using this data, output
# the galaxy with the slowest velocity, and the galaxy with the highest velocity.

# with open('starter/galaxies.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     slow = [None, float('inf')]    #ignores first. Variable value = infinity (huge) 
#     fast = [None, 0]   #ignores first. Variable value = 0 (low)
#     for i, row in enumerate(csv_reader):    #i means index (naming convention). Row is row.
#         if i != 0:  #this first 'if' in the loop ensures each value is checked when the loop iterates because no rows = 0.
#             if int(row[1]) < slow[1]: #this 'if' (within the first'if') targets velocity data in each row: e.g. row[1] for row (18,19349) gets (19349). If velocity value is less than current slow value, do this:
#                 slow =  [row[0], int(row[1])]  #this line re-defines the slow var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be lower than the last one stored)
            
#             if int(row[1])> fast[1]: #this 'if' (within the first'if') says if velocity is greater than current fast value, do this:
#                 fast = [row[0], int(row[1])] #this line re-defines the fast var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be faster than the last one stored)
    
#     print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.') #formatted print returns the new slow variable - galaxy + value
#     print(f'Galaxy {fast[0]} has a max velocity of {fast[1]}km/sec.') #formatted print returns the new fast variable - galaxy + val
