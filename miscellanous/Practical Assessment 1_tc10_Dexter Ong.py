#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "day 1"
name = "Dexter Ong Khoo Shian"
np_email = "s10241948@connect.np.edu.sg"
student_id = "S10241948D"
class_number = "TC10"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.


#------------------------ Challenge 1 ------------------------------#
def acceleration_function(final_velocity, starting_velocity, elapsed_time):
    #determine the subtraction of initial velocity from final velocity and store in variable called
    velocity = final_velocity - starting_velocity
    #find average acceleration by dividing new variable velocity with elasped time
    average_acceleration = velocity/elapsed_time
    #format and return average acceleration and round it to 2dp
    return(f"Drone acceleration = {round(average_acceleration,2)} meters per second")

print(acceleration_function(final_velocity=20, starting_velocity=5, elapsed_time=10))
print(acceleration_function(final_velocity=30, starting_velocity=4, elapsed_time=9))

#------------------------ Challenge 2 ------------------------------#
def check_pw(password):
    #define 2 new variables uppercase and lowercase to be False so as to check for upper and lower case later
    uppercase = False
    lowercase = False
    #use len function to ensure that length of password is not less than 14, if it is, then weak password is automatically returned
    if len(password) < 14:
        return("weak password")
    else:
        #use for loop to iterate through characters in password string
        for i in password:
            #check for uppercase letters in password variable, it present, uppercase variable will be updated to true
            if i.isupper() == True:
                uppercase = True
            #check for lowercase letters in password, if present lowercase variable will be updated to True
            elif i.islower() == True:
                lowercase = True
        #check that if both uppercase and lowercase variable are true along with at least 14 characters, password will be considered strong
        if uppercase == True and lowercase == True:
            return("strong password")
        #if either uppercase or lowercase variable return false, then weak password will be returned
        else:
            return("weak password")

print(check_pw("NgeeAnnPolytechnic"))
print(check_pw("NgeeannpolytechniC"))
print(check_pw("ngeeannpolytechnic"))
print(check_pw("NgeeAnn"))
print(check_pw("ngeeann"))
