# Instructions
# Given a number, find the sum of all the unique multiples of particular numbers up to but not including that number.

# If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

# The sum of these multiples is 78.

# You can make the following assumptions about the inputs to the sum_of_multiples function:

# All input numbers are non-negative ints, i.e. natural numbers including zero.
# A list of factors must be given, and its elements are unique and sorted in ascending order.

def sum_of_multiples(limit, multiples):
    if 0 in multiples:
        multiples.remove(0)            
    x = []
    for i,j in zip(multiples, range(0,len(multiples))):
        while i<limit:
            x.append(i)
            i+=multiples[j]
    print(x)
    return sum(set(x))

