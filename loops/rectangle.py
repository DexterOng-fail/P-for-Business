width = input("enter height: ")
height = input("enter width: ")
unit = input("enter unit: ")

while True:
    if width.isdigit() == False:
        print("please renter!!!")
        width = input("enter width: ")
    else:
        if height.isdigit() == False:
            print("please renter!!!")
            height = input("enter height: ")
        else:
            height = int(height)
            width = int(width)
            area = width*height
            break
print("the area of rectangle is {}{}".format(area, unit))