from pathlib import Path
import csv
file_path = Path.home()/'pyhton4biz'/'dbs_shares.csv'
file_path.touch()
print(file_path.exists())
empty_list = []
with file_path.open(mode = "r", encoding = "UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line)
        for value in line:
            empty_list.append(value)

print(empty_list)
   