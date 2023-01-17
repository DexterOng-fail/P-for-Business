from pathlib import Path
import csv
file_path = Path.home()/'pyhton4biz'/'numbers.csv'
file_path.touch()
numbers = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30]]

with file_path.open(mode = 'r', encoding='UTF-8', newline="") as file:
    reader = csv.reader(file)
    for num in reader:
        print(num)
#  writer = csv.writer(file)
#    for i in numbers:
#     writer.writerow(i)