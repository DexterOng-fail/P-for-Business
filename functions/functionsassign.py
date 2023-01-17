#1
import math
print(math.sqrt(450))
#2
print(int(math.floor(423.89)))
#3
# The help function
#4
USD = input("Your USD: ")
def convertUSD_SGD(USD):
    USD = int(USD)
    SGD = USD*1.075
    return(SGD)
print(convertUSD_SGD(USD))
#5
counter = 0
def addNumber(x):
    global counter
    counter = counter + x
    return(counter)
print(addNumber(10))
print(addNumber(10))


#6
def greet():
    return("Good morning!")
print(greet())

#7
name = input("Enter name: ")
def greetNAME(name):
    return(f"good morning {name}")
print(greetNAME(name))

#8
def bmi(weight, height):
    newheight = height**2
    mybmi = weight/newheight
    return mybmi   
height = float(input("Enter your height: "))
weight = float(input("enter your weight: "))
print(f"my bmi is {bmi(weight, height)}")

#9
def bmi2(height, weight):
    mybmi = weight/(height**2)
    return mybmi
print(bmi2(1.52, 60))