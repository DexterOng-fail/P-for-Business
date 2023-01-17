from pathlib import Path
home = Path.home()
newdata = ["\n" "weight: 71", "\n" "height: 175"]
file_path1 = home/"pyhton4biz"/"test.txt.txt"
file_path2 = home/"pyhton4biz"/"context.txt"
print(file_path1.exists())
with file_path1.open(mode = "r", encoding = "UTF-8" ) as file:
    for i in file.readlines():
        print(i)
        text = file.read()
print(text)

with file_path2.open(mode = "a", encoding = "UTF-8") as file:
    file.writelines(newdata)
