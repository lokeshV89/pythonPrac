import csv

with open('1000Records.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    line_count = 0
    for line in csv_reader:
        print(line)