#1
num = int(input("Enter num: "))
for i in range(num+1):
    ih = i**2
    print(f"the square of {i} is {ih}")

#2
def factorial():
    num2 = int(input("Enter num2: "))
    total = 1
    for i in range(1,num2+1): 
        total = i*(total)
    return(f"The factorial of 5 is {total}")
print(factorial())

#3
def loop():
    x = 1
    while x < 6:
        print(f"double of loop {x} is {x*2}")
        x = x+1
print(loop())

#4
user_id = "ba_admin"
user = input("please input id: ")
while user != user_id:
    user = input("Incorrect id, enter again : ")
else:
    print("Log in successful")
