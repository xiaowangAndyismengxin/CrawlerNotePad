import csv


with open('data.csv') as f:
    csv_content = csv.reader(f)
    print(csv_content)
    for i in csv_content:
        print(i, type(i))
