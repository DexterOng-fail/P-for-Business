#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "functions and loops"
#name = "Dexter Ong Khoo Shian"
#np_email = "s10241948@connect.np.edu.sg"
#student_id = "S10241948D"
#class_number = "TC10"

#-------------------------------- Q1 ------------------------------------#
# Write a program that allow users to calculate distance, time, speed.
#------------------------------------------------------------------------#

# The program should include 3 functions:

    #### speed_function() ####
    # speed = distance/time

    #### distance_function() ####
    # distance = time * speed

    #### time_function() ####
    # time = distance/speed

# The functions will round float to 2 decimal places.

# When the 3 functions are executed, they should display and return:

    ##### Example of speed_function() #####
    ## Enter distance (in km): 10
    ## Enter time taken (in hours): 2
    ## Based on the distance and time input, the calculated speed (km/hr) = 5.0
    
    ##### Example of distance_function() #####
    ## Enter time taken (in hr): 2
    ## Enter speed (in km/hr): 5
    ## Based on the speed and time input, the calculated distance (km) =  10.0

    ##### Example of time_function() #####
    ## Enter distance (in km): 10
    ## Enter speed (in km/hr): 5
    ## Based on the speed and distance input, time taken (in hr) = 2.0


def speed_function():
    """
    - Function calculates speed based on input of distance and time
    """
    #get user input for distance
    distance = float(input("Enter Distance (in km): "))
    #get user input for time
    time = float(input("Enter time taken (in hours): "))
    #find the speed using distance divide by time
    speed = distance/time
    #round the time to 2dp
    speed = round(speed, 2)
    #print the formatted output for speed after calculation
    return(f"Based on the distance and time input, the calculated speed (km/hr) = {speed}")
#print the function (speed_function)
print(speed_function())



def distance_function():
    """
    - Function calculates distance based on input of speed and time
    """
    #get user input for time
    time = float(input("Enter time taken (in hr): "))
    #get user input for speed
    speed = float(input("Enter speed (in km/hr): "))
    #calculate distance by multiplying time with speed
    distance = time * speed
    #round distance down to 2dp
    distance = round(distance, 2)
    #print the formatted output for distance after calculation
    return(f"Based on the speed and time input, the calculated distance (km) = {distance}")
#print the function (distance_function)
print(distance_function())

def time_function():
    """
    - Function calculates time taken based on input of distance and speed
    """
    #get user input for distance
    distance = float(input("Enter distance (in km): "))
    #get user input for speed
    speed =  float(input("Enter speed (in km/hr): "))
    #calculate time by dividing distance by speed
    time = distance/speed
    #round time down to 2dp
    time = round(time, 2)
    #print the formatted output for time after calculation
    return(f"Based on the speed and distance input, time taken (in hr) = {time} ")
#print the function (time_function)
print(time_function())
