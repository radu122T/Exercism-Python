# Instructions
# Given a string of digits, output all the contiguous substrings of length n in that string in the order that they appear.

# For example, the string "49142" has the following 3-digit series:

# "491"
# "914"
# "142"
# And the following 4-digit series:

# "4914"
# "9142"
# And if you ask for a 6-digit series from a 5-digit string, you deserve whatever you get.

# Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically consecutive.

# Exception messages
# Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

# This particular exercise requires that you use the raise statement to "throw" a ValueError if the series and/or length parameters input into the slice() function are empty or out of range. The tests will only pass if you both raise the exception and include a message with it.

# To raise a ValueError with a message, write the message as an argument to the exception type:

# # if the slice length is zero.
# raise ValueError("slice length cannot be zero")

# # if the slice length is negative.
# raise ValueError("slice length cannot be negative")

# # if the series provided is empty.
# raise ValueError("series cannot be empty")

# # if the slice length is longer than the series.
# raise ValueError("slice length cannot be greater than series length")

def slices(series, length):
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    elif length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0 :
        raise ValueError("slice length cannot be negative")
    elif length>len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        x = [series[j:i] for i, j in zip(range(length,len(series)+1), range(0,len(series)+1))]
        return x