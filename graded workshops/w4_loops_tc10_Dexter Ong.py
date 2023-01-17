#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "loops"
#name = "Dexter Ong"
#np_email = "s10241948@connect.np.edu.sg"
#student_id = "s10241948D"
#class_number = "TC10"

#-------------------------------- Q2 ------------------------------------#
# Write a function: loan_calculator(amount, interest, month).
# The function will calculate the total loan amount payable.
#------------------------------------------------------------------------#

#### Example of how the function works ####

# Given a loan amount of $1000, 10% interest rate and 5 month loan period,
# the function will calculate the interests payment plus the principal loan amount.
# When `loan_calculator(1000,0.10,5)` is executed, it will return $1610.51

# The calculation of $1610.51 is as follow:
# Month 1 = $1100 ($1000 * 1.1)
# Month 2 = $1210 ($1100 * 1.1)
# Month 3 = $1331 ($1210 * 1.1)
# Month 4 = $1464.1 ($1331 * 1.1)
# Month 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.
# BONUS: Can you use f-strings to include a $ symbol with the return value?
def loan_calculator(amount, interest, month):
    """
    Describe what the function does and what parameters are required
    """
    #use for loop to check all the loops
    for i in range(month):
        #find the new amount after adding old amount with interest
        newamount = amount + (amount*interest)
        #make python store the old amount
        oldamount =  amount
        #set the new amount as amount to run the loop again
        amount = newamount
        #print out the formatted string
        print(f"Month {i+1} = ${round(amount,2)} (${round(oldamount,2)} * {round(interest,2)})")
        
loan_calculator(1000,0.10,5)
loan_calculator(5000,0.15,8)