#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "Data Structure"
#name = "Dexter ong"
#np_email ="s10241948@connect.np.edu.sg"
#student_id = "S10241948D"
#class_number = "TC10"

#--------------------- 1. List ---------------------#

# You are given information of the membership numbers and the membership fees of the local gyms.
# The information is a nested list `gym_data`. The elements in each sub-list contain:
## 1. The gym name
## 2. The number of members
## 3. Membership fee per member

gym_data_list = [['FitFirst', 8500, 3500], ['PlanetFit', 5500, 2300], [
    'GoldGym', 9000, 1800], ['AnyTimeFit', 7200, 2400], ['VirginFit', 3200, 3800]]

# 1.
# Write a function `total_summary_list` with a single parameter `option`.
# When "membership" is supplied to the option parameter, `total_summary_list` function will return
# the total number of membership across the gyms.
# When "fee" is supplied to the option parameter, `total_summary_list` function will return
# the total membership fee revenue collected across the gyms.
# Otherwise, it will return `invalid entry` for any other values supplied to the `option` parameter.
# Note: total membership fee revenue =  the number of members x membership fee per member

''''''

def total_summary_list(option):
    #create a variable to store total number of members and fee and set membership to 0
    total_membership = 0
    fee = 0
    #ensure option is all lowercase and check that its value equals to membership
    if option.lower() == "membership":
        #create for loop to iterate through gym data list
        for a in gym_data_list:
            #sum all values of member and store it in total membership value
            total_membership = total_membership + int(a[1])
        #format and print out total membership
        return(f"total number of members across the gyms: {total_membership}")
    #ensure option is all lowercase and check that its value equals to fee
    elif option.lower() == "fee":
        #create for loop to iterate through gym data list
        for b in gym_data_list:
            #get the value of revenue by mutiplying membership fee with no of members and store it in fee
            fee += (int(b[1])*int(b[2]))
        #format and print out total membership fee revenue 
        return(f"Total membership fees revenue collected across the gyms: ${fee}")
    #check for any other values of option and return invalid entry
    else:
        return("invalid entry")

print(total_summary_list("membership"))

# Examples of what the functions will display and return when executed:

## print(total_summary_list("membership"))
## Total number of members across the gyms: 33400


## print(total_summary_list("fee"))
## Total membership fees revenue collected across the gyms: $88040000

#--------------------- 2. Dictionary ---------------------#
# The same information is now structured as a dictionary.
# Write a similar function that will total number of membership and
# total membership fee revenue.

gym_data_dict = {'FitFirst': {"number of members": 8500,
                              "membership fee": 3500
                              },
                 "PlanetFit": {"number of members": 5500,
                               "membership fee": 2300
                               },
                 "GoldGym":  {"number of members": 9000,
                              "membership fee": 1800
                              },
                 "AnyTimeFit": {"number of members": 7200,
                                "membership fee": 2400
                                },
                 "VirginFit": {"number of members": 3200,
                               "membership fee": 3800
                               },
                 }


def total_summary_dict(option):
    #create a variable to store total number of members and fee and set membership to 0
    total_membership = 0
    fee = 0
    #ensure that the option is lowercase and is membership
    if option.lower() == "membership":
        #iterate through dictionary gym data dict
        for place in gym_data_dict:
            #find total number of members across all gyms by adding all keys of gym places in gym data dict and store it in total membership
            total_membership = total_membership + (gym_data_dict[place]["number of members"])
        #format and print out total membership
        return(f"total number of members across the gyms: {total_membership}")
   #ensure that the option is lowercase and is fee
    elif option.lower() == "fee":
        #iterate through dictionary gym data dict
        for place in gym_data_dict:
            #find total membership revenue fee across all gyms by adding all keys of gym places in gym data dict and store it in fee
            fee = fee + (gym_data_dict[place]["membership fee"])*(gym_data_dict[place]["number of members"])
        #format and print out total membership
        return(f"Total membership fees revenue collected across the gyms: ${fee}")
    #check for any other values of option and return invalid entry
    else:
        return("invalid entry")
              
    
print(total_summary_dict("fee"))
# Examples of the functions when executed:

    ## print(total_summary_dict("membership"))
    ## Total number of members across the gyms: 33400

    ## print(total_summary_dict("fee"))
    ## Total membership fees revenue collected across the gyms: $88040000
