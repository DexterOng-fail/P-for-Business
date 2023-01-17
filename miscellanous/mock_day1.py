#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "mock time based practical"
name = "Dexter ong"
np_email = "s10241948@connect.np.edu.sg"
student_id = "s10241948D"
class_number = "TC10"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

#1
def bp(systolic, diastolic):
    if systolic > 180 or diastolic > 120:
        bp_category = "Hypertension Crisis"
    elif systolic >= 140 or diastolic >= 90:
        bp_category = "Hypertension Stage 2"
    elif systolic >= 130 or diastolic >= 80:
        bp_category = "Hypertension Stage 1"
    elif systolic >= 120 and diastolic < 80:
        bp_category = "Elevated"
    else:
        bp_category ="Normal"
    return(f"Systolic: {systolic} | Diastolic: {diastolic} | {bp_category}")

print(bp(110, 75))
print(bp(134, 79))
print(bp(134, 70)) 
print(bp(150, 90))
print(bp(181,100))

#2
def emoticon(mood):
    if mood == "surprise":
        return("i feel... :o")
    elif mood == "cheeky":
        return("i feel... ;)")
    elif mood == "naughty":
        return("i feel... :P")
    elif mood == "smiley":
        return("i feel... :)")
    elif mood == "moody":
        return("i feel... :(")
    elif mood == "happy":
        return("i feel... =)")
    else:
        return("No such emoticons!")
print(emoticon("sad"))