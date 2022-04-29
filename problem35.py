# Instructions
# Determine if a triangle is equilateral, isosceles, or scalene.

# An equilateral triangle has all three sides the same length.

# An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

# A scalene triangle has all sides of different lengths.

# Note
# For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side. See Triangle Inequality.

# Dig Deeper
# The case where the sum of the lengths of two sides equals that of the third is known as a degenerate triangle - it has zero area and looks like a single line. Feel free to add your own code/tests to check for degenerate triangles.


def equilateral(sides):
    for i in sides:
        if i != 0 and sides.count(i) == 3:
            return True
    return False
        


def isosceles(sides):
    for i in set(sides): 
        if i != 0 and min(set(sides))*2>(max(sides)) and 1<=len(set(sides))<=2:
            return True
    return False


def scalene(sides):
    for i in sides: 
        if i != 0 and sides[0]!=sides[1]!=sides[2] and sorted(sides)[0]+sorted(sides)[1]>=sorted(sides)[2] :
            return True
    return False

    
