"""
Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.
"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)
integer = 5
print(integer)
print(type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number
float = 1.79
print(float)
print(type(float))

# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes
word = "this is a string"
print(word)
print(type(word))

# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int
float_num = 5.5
int_num = int(float_num)
print(int_num)
print(type(int_num))

# TODO: Cast int to string
number = 5
print("this is the number " + str(number))
print(type(number))
# TODO: Cast number string to int
numb = "5"
total = int(numb) + 2
print(total)
print(type(total))
# TODO: Input demo (str to float)
