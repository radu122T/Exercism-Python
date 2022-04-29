# Instructions
# Given a string representing a matrix of numbers, return the rows and columns of that matrix.

# So given a string with embedded newlines like:

# 9 8 7
# 5 3 2
# 6 6 7
# representing this matrix:

#     1  2  3
#   |---------
# 1 | 9  8  7
# 2 | 5  3  2
# 3 | 6  6  7
# your code should be able to spit out:

# A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
# A list of the columns, reading each column top-to-bottom while moving from left-to-right.
# The rows for our example matrix:

# 9, 8, 7
# 5, 3, 2
# 6, 6, 7
# And its columns:

# 9, 5, 6
# 8, 3, 6
# 7, 2, 7
# In this exercise you're going to create a class. Don't worry, it's not as complicated as you think!

# A First Look at Classes from the Python 3 documentation.
# How to Define a Class in Python from the Real Python website.
# Data Structures in Python from the Python 3 documentation.

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [list(map(int,i.split())) for i in matrix_string.splitlines()]
    def row(self, index):
        return self.matrix_string[index-1]
    
    def column(self, index):
        return [row[index-1] for row in self.matrix_string]
