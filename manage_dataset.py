import csv

files = ["csv_ca-500.csv", "csv_au-500.csv", "csv_uk-500.csv", "csv_us-500.csv"]
last_name_set = set()
first_name_set = set()

for i in files:
    f = open('/Users/edwyn/Downloads/{}'.format(i))
    reader = csv.reader(f)
    next(reader)

    for j in reader:
        last_name_set.add(j[1])
        first_name_set.add(j[0])

with open('lastName.txt', 'w') as file:
    for i in last_name_set:
        file.write('{}\n'.format(i))

with open('firstName.txt', 'w') as file:
    for i in first_name_set:
        file.write('{}\n'.format(i))
