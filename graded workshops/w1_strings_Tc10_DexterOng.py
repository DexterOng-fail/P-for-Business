#####  Store your, name, email, student_id and class_number as STRINGS #####
#exercise = "strings"
#name = "Dexter Ong"
#np_email = "s10241948@connect.np.edu.sg"
#student_id = "s10241948D"
#class_number = "TC10"

# ---------- Write a program to allow a user to enter some text ----------#

# The program will:
    # 1. Convert any uppercase strings to lowercase strings.
    # 2. After step 1, it will replace lowercase character of z, b, t, g, h with 1, 2, 3, 4, 5 respectively.

# When your program file is executed, it will look like this:

   # Enter some text in uppercase: I LOVE SINGAPORE ZOO BEST
    # Converted your text to lower case: i love singapore zoo best
    # Replaced any character of z, b, t, g, h with 1, 2, 3, 4, 5: i love sin4apore 1oo 2es3

# You should assign a variable and named it as `text` to store the user input.

# Note:
# `I LOVE SINGAPORE` is the user input text.
# `i love singapore` and `i love sin4apore` are the output of the program

#1
phrase = input("Enter your text: ")
phrase = phrase.lower()
print(f"Converted text to lower text: {phrase}")
#2
phrase1 = phrase.replace("z", "1")
phrase2 = phrase1.replace("b", "2")
phrase3 = phrase2.replace("t", "3")
phrase4 = phrase3.replace("g", "4")
phrase5 = phrase4.replace("h", "5")
print("Replaced any character of z, b, t, g, h with 1, 2, 3, 4, 5: {}".format(phrase5))

