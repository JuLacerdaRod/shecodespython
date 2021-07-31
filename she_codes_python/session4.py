import csv

asli_said= []

with open("dogs_are_awesome.txt") as csv_file:
    csv_reader = csv.reader(csv_file)  #creates the reader object
