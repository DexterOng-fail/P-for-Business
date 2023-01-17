from pathlib import Path
import csv
file_path = Path.home()/'pyhton4biz'/'weather.csv'
file_path.touch()
weather = [["Monday", 28.7, 10], ["Tuesday", 30.2, 15],  ["Wednesday", 32, 9], ["Thursday", 26, 19],  ["Friday", 28, 14]]
header = ["Day", "Temperature", "Wind Speed"]
weather_list = []
with file_path.open(mode = "r", encoding = "UTF-8", newline="") as file:
    # writer = csv.writer(file)
     #writer.writerow(header)
    # for w in weather:
    #    writer.writerow(w)
    reader = csv.reader(file)
    next(reader)
    for day, temp, windspeed in reader:
        empty_dict = dict()
        empty_dict["day"] = day
        empty_dict["temp"] = temp
        empty_dict["windspeed"] = windspeed
        weather_list.append(empty_dict)
print(weather_list)