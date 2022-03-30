import csv
reader = csv.DictReader(open("Medicalpremium.csv"))

for row in reader:
    print(row)

