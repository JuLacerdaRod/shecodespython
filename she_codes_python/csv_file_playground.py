import csv

# with open("2016_pilbara.csv") as csv_file:       # or data/2016_pilbara.csv if in folder data
#     csv_reader = csv.reader(csv_file)   #  delimiter="," is default / delimiter="-"
#     for line in csv_reader:
#         print(line)

# list of lists

with open("2016_pilbara.csv", mode="r", encoding="utf-8") as csv_file:       # or data/2016_pilbara.csv if in folder data
    csv_reader = csv.reader(csv_file, delimiter="")   #  delime=iter="," is default / delimeter="-"
    for line in csv_reader:
        population.append(line)

# print(population)

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")

with open("population.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for age_group in population:
        csv_writer.writerow([age_group[0], age_group[1]])