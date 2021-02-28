import csv

with open('1000Records.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    line_count = 0
    for line in csv_reader:
        #if we want to remove header
        if line_count == 0:
            
            line_count += 1
        else:
            print(line)
            # it want to print specific index line
            #print(line[2])