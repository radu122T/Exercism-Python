# Instructions
# The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8

# ISBN
# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

# (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
# If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

# Example
# Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
# Since the result is 0, this proves that our ISBN is valid.

# Task
# Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

# The program should be able to verify ISBN-10 both with and without separating dashes.

# Caveats
# Converting from strings to numbers can be tricky in certain languages. Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.

# Bonus tasks
# Generate a valid ISBN-13 from the input ISBN-10 (and maybe verify it again with a derived verifier).

# Generate valid ISBN, maybe even from a given starting ISBN.

def is_valid(isbn):
    if len(isbn) == 0:
        return False
    new_list = list(isbn.replace("-","").upper())
    if new_list[-1] == "X":
        new_list.pop(-1)
        new_list.append("10")
    for i in new_list:
        if not i.isnumeric():
            return False
    if len(new_list) != 10:
        return False
    
    return (int(new_list[0]) * 10 + int(new_list[1]) * 9 + int(new_list[2]) * 8 + int(new_list[3]) * 7 + int(new_list[4]) * 6 + int(new_list[5]) * 5 + int(new_list[6]) * 4 + int(new_list[7]) * 3 + int(new_list[8]) * 2 + int(new_list[9]) * 1) % 11 == 0
 
