#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "numbers"
#name = "Dexter Ong"
#np_email = "s10241948@connect.np.edu.sg"
#student_id = "s10241948D"
#class_number = "TC10"

#-------------------------------- Q1 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.    
# The program will check if the sum between these 2 numbers is an integer. 
#----------------------------------------------------------------------------#

# The program should display message like the following when executed.

    #------ First execution ------#
    # Enter first number : 3.5
    # Enter second number : 1.5
    # 3.5 + 1.5 = 5.0
    # Is the sum of 3.5 and 1.5 an integer? True

    #------ Second execution ------#
    # Enter first number : 3.5
    # Enter second number : 2.3
    # 3.5 + 2.3 = 5.8
    # Is the sum of 3.5 and 2.3 an integer? False

# In the first execution, the input values are  3.5 and 1.5
# In the second execution, the input values are 3.5 and 2.3
# The program will sum the 2 numbers and return True when the sum is an integer or False when sum is a float.

# Assign `num1` as a variable for the first number, `num2` as a variable for the second number
# Assign `sum_num` as the variable to store the arithmatic operation between `num1` and `num2`  

#ask for input of first number
num1 = float(input("Enter first number: "))
#ask for input of second number
num2 = float(input("enter second number: "))
#find the sum of num1 and num2
sum_num = num1 + num2
#check if sum_num is an integer
var = sum_num.is_integer()
#print the sum of num1 and num2 is sum_num
print(f"{num1} + {num2} = {sum_num}")
#print out the result of whether if sum_num is an integer
print(f"Is the sum of {num1} and {num2} an integer? {var}")

#-------------------------------- Q2 ----------------------------------------#
# Write a program to ask user to input two numbers using 2 input functions.  
# The program will use the first number as dividend and second number as a divisor.
# The output should return the remainder of the division. 
#----------------------------------------------------------------------------#

# The program should display the following messages :

    # Enter a dividend: 30
    # Enter a divisor: 3
    # The remainder is 0.0

# In the execution above, the input values are  30  and 3. The program will return the remainder of 30 divided 3.

# Assign `num3` for the dividend and `num4` for the divisor.
# Assign 'modulus` to store the results of the operation.

#ask for input of num3 in float type
num3 = float(input("Enter a dividend: "))
#ask for input of num4 in float type
num4 = float(input("Enter a divisor: "))
#find the remainder of the division of num3 by num4
modulus = num3%num4
#print out the remainder of the division of num3 by num4
print(f"the remainder is {modulus}")
