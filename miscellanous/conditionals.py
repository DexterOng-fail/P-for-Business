#1
print(4 > 2)

print(5 < 10)

print("python" != "C++")

print(50 != "50")

#2
print(False == (not True))
print((True and False) == (True and False))
print(not (True and "A" == "B"))

#3
school = "business and accountancy"
if school == "business and accountancy":
    print("business and accountancy")
elif school.lower() == 'ba':
    print(school)
else:
     print("invalid entry")

#4
apple_price = float(input("enter apple price: "))
orange_price = float(input("enter orange price: "))
if apple_price > orange_price:
    print("apple price is higher than orange")
elif apple_price < orange_price:
    print("orange price is higher than apple")
else:
    print("apple and orange prices are equal")
#5
height = float(input("Enter your height: "))
if height >= 175:
    print("tall")
elif 165 <= height < 175:
    print("average")
else:
    print("short")
#6
gender = input("Enter your gender: ")
hair_length = "long"
if gender == "female" and hair_length == "long":
    print("tie up your hair")
elif gender == "female" and hair_length == "short":
    print("style your hair")
elif gender == "male" and hair_length == "long":
    print("cut your hair")
else:
    print("comb your hair")

#7
for value in range(21):
    if value == 1:
        print(f'{value} is first value')
    elif value ==  10:
        print(f"{value} is middle value")
    elif value == 20:
        print(f"{value} is last value")

#8
for index, value in enumerate(range(80,150)):
    print(index, value)
    if index == 20:
        break
#9
def height_func():
    while True:
        try:
            user_input = float(input("enter your height in m: "))
        except ValueError:
            print("your input is invalid, please try again")
        else:
            print(f"your height of {user_input} in metre is {user_input*3.28084} in feet")
            break
height_func()

#10
