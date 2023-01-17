#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "day 2"
name = "Dexter Ong"
np_email = "s10241948@connect.np.edu.sg"
student_id = "S10241948D"
class_number = "TC10"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

#------------------------ Challenge 1 ------------------------------#
def waist_hip():
    #get the user input for gender and turn it into uppercase
    gender = (input("What is your gender (M or F)?:  ")).upper()
    #get the user inputs for waist and hip measurement in float format 
    waist = float(input("What is your waist measurement (inches)?: "))
    hip = float(input("What is your hip measurement (inches)?: "))
    #find the value of waist hip measurement by dividing waist measurement by hip measurement
    WHR = round(waist/hip, 2)
    #set the parameter if gender entered is male, the measurements below will be used
    if gender == "M":
        #determine based on the value of WHR, whether the health risk is low medium or high and store that value into a variable called health_risk
        if WHR < 0.9:
            health_risk = "low"
        #if calculated WHR is between 0.9 and 0.99 and gender is M, health risk will be medium
        elif 0.9 <= WHR <= 0.99:
            health_risk = 'Medium'
        #if calculated WHR is one and above and gender is M, health risk will be high
        elif WHR >= 1:
            health_risk = "high"
    #set the parameter for gender = female so as to specify which measurements to be used
    elif gender == "F":
        #determine based on the value of WHR and the input of female, what the health risk is
        #if calculated WHR is below 0.8 and gender is F, health risk will be low
        if WHR < 0.8:
            health_risk ="low"
        #if calculated WHR is between 0.8 and 0.89 and gender is F, health risk will be medium
        elif 0.8 <= WHR <= 0.89:
            health_risk = "medium"
        #if calculated WHR is above 0.9 and gender is F, health risk will be high
        elif WHR >= 0.9:
            health_risk = "high"
    #print out the waist hip ratio and the health risk in formatted string format
    return(f"Your Waist hip ratio is {WHR}\nYour health risk: {health_risk}")
print(waist_hip())

#------------------------ Challenge 2 ------------------------------#
def calc_age(age):
    #check that age is not a negative number and return input if it is
    if float(age) < 0:
        return("Age cannot be negative a number")
    #if age is positive
    else:
        #mutiply the age in years with 365 and return the formatted string
        age_days = age*365
        return(f"{age} years is equal to {age_days} days")
print(calc_age(40))
