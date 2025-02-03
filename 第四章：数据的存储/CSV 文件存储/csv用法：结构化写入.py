import csv


fieldnames = ['id', 'name', 'age']
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': None, 'name': 'Bob', 'age': 18})
    writer.writerow({'id': 2, 'name': 'Ben', 'age': 27})
    writer.writerows([
        {'id': 3, 'name': 'Benb', 'age': 27},
        {'id': 4, 'name': 'Bent', 'age': 27}
    ])
