import csv

# open  a new file in write mode
with open('new_csv_file.csv',mode ='w') as new_file:
    csv_writer = csv.writer(new_file,delimiter='\t')
    
    # read the new file for writing
    with open('1000Records.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            csv_writer.writerow(line)