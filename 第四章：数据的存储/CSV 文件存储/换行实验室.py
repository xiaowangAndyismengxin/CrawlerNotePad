import csv


file_name = 'enter_experiment.txt'
newline = None
with open(file_name, 'w', encoding='UTF-8', newline=newline) as f:
    f.write('\r\n')

with open(file_name, 'r', encoding='UTF-8', newline=newline) as f:
    print(repr(f.read()))

with open(file_name, 'rb') as f:
    print(f.read())

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow([1, 'Bob', 17])
    writer.writerow([2, 'Ben', 27])
with open('data.csv', 'rb') as csvfile:
    print(csvfile.read())
