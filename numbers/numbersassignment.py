#1-4
import math
num1 = 5_000_000_000
num2 = 100.5
num3 = "200.50"
gg = type(num1)
ff = type(num2)
cc = type(num3)
print(f"num1 is a {gg}, num2 is a {ff}, num3 is a {cc}")

#5
num3 = float(num3)
print(float(num2 + num3))

#6 -7
num4 = 50
print(num2/num4)
#8
print(num2%num4)
#9
print(4**5)
#10
num5 = (num2*num4) + float(num3)
print(num5)
#11
print((num2+num4)*float(num3))
#12
print(round(2.02454, 2))
#13
num6 = math.floor(1000.40)
print(num6)
#14
pow(4, 5)
#15
num7 = float(input("Enter your first number: "))
num8 = float(input("enter your second number: "))
print(f"addition results: {num7+num8}\n subtraction results: {num7-num8}\n Multiplication results: {num7*num8}\n Division results: {num7/num8}")