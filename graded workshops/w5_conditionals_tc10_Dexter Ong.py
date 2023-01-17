#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "conditionals"
#name = "Dexter Ong"
#np_email = "s10241948@connect.np.edu.sg"
#student_id = "s10241948D"
#class_number = "TC10"

#------------------------ Part 1 : if, elif, else ------------------------#
# Write a function: tax_rebate() to determine tax rebate from income level
#-------------------------------------------------------------------------#

# The function will prompt a user to declare his/her yearly income
# and determine the amount of one-time off tax rebate he/she should receive.
# Note that the function does not require any parameters. It will return the
# amount of tax rebate based on the following tax rules:

# Yearly Income in $ 	                # Tax Rebate in $
# ------------------                      -------------
# 0 to less than 40000 	                      2000
# 40000 to less than 100000	                  1000
# 100000 to less than 150000 	              500
# equal or greater than 150000 	             not eligible

# Executing the function based om different income levels will display and return output
# like the followings:

#### Example 1 ####
# Declare your yearly income : 10000
# Your tax rebate is : $2000

#### Example 2 ####
# Declare your yearly income : 80000
# Your tax rebate is : $1000

#### Example 3 ####
# Declare your yearly income : 110000
# Your tax rebate is : $500

#### Example 4 ####
# Declare your yearly income : 150000
# You are not eligible for tax rebate

#### Example 5 ####
# Declare your yearly income : 200000
# You are not eligible for tax rebate

def tax_rebate():
    """
    - function will return rebate based on income level
    """
    #prompt user input for yearly income
    yearly_income = float(input("please enter your yearly income: "))
    #check if user input for yearly income is between 0 and 40000
    if 0 <= yearly_income < 40000:
        #return tax rebate for yearly income for yearly income between 0 and 40000
        return("Your tax rebate is: $2000")
    #check if user input for yearly income is between 40000 and 100000
    elif 40000 <= yearly_income < 100000:
        #return tax rebate for yearly income for yearly income between 40000 and 100000
        return("Your tax rebate is: $1000")
    #check if user input for yearly income is between 100000 and 150000
    elif 100000 <= yearly_income < 150000:
        #return tax rebate for yearly income for yearly income between 100000 and 150000
        return("Your tax rebate is: $500")
    #check if user input for yearly income is 150000 and above
    else:
        #return tax rebate for yearly income for yearly income for 150000 and above
        return("You are not eligible for tax rebate")
#call function
print(tax_rebate())

#---------------------------------- Part 2  ---------------------------------#
# Improve the tax_rebate() function from Part 1 to make the program
# less susceptible to crashing.
#----------------------------------------------------------------------------#

# It should prevent the program from crashing if the user entered "string"
# data type when declaring his/her income.

# The function should loop endlessly to ask the user to declare the income until
# he/she use "number" data type.

# Here is an example of how the program will behave:

    # Declare your yearly income: ten thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: one thousand
    # [INVALID INPUT] Only number is accepted, please re-enter again.
    # Declare your yearly income: 10000
    # Your tax rebate is : $2000

# Tips:
# Design the function with `while loop` in mind, so that program will
# keep looping until the user input entered the correct data type.


def tax_rebate_2():
    """
    - Function will return rebate based on income level
    """
    #prompt user for user input
    yearly_income = input("please enter your yearly income: ")
    #start the while loop to check if user input is integer
    while True:
        #check if yearly_income is int format
        if yearly_income.isdigit() == False:
            #output warning to tell user that input is not integer
            print("[INVALID INPUT] Only number is accepted, please re-enter again.")
            #prompt for user input again
            yearly_income = input("please enter your yearly income: ")
        #if all variables are correct
        else:
            #change character type for yearly income to int
            yearly_income = int(yearly_income)
            #check number range of yearly income
            if 0 <= yearly_income < 40000:
                #return tax rebate
                return("Your tax rebate is: $2000")
            #check number range of yearly income
            elif 40000 <= yearly_income < 100000:
                #return tax rebate
                return("Your tax rebate is: $1000")
            #check number range of yearly income
            elif 100000 <= yearly_income < 150000:
                #return tax rebate
                return("Your tax rebate is: $500")
            #check number range of yearly income
            else:
                #return tax rebate
                return("You are not eligible for tax rebate")
#call function
print(tax_rebate_2())
