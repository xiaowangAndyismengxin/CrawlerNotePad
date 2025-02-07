import csv


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow([1, 'Bob', 17])
    writer.writerow([2, 'Ben', 27])
    writer.writerows(
        [
            [3, 'xiaoming', 13],
            [4, 'xwA', 12]
        ]
    )
