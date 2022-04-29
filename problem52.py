# Instructions
# There are 10 types of people in the world: Those who understand binary, and those who don't.

# You and your fellow cohort of those in the "know" when it comes to binary decide to come up with a secret "handshake".

# 1 = wink
# 10 = double blink
# 100 = close your eyes
# 1000 = jump


# 10000 = Reverse the order of the operations in the secret handshake.
# Given a decimal number, convert it to the appropriate sequence of events for a secret handshake.

# Here's a couple of examples:

# Given the input 3, the function would return the array ["wink", "double blink"] because 3 is 11 in binary.

# Given the input 19, the function would return the array ["double blink", "wink"] because 19 is 10011 in binary. Notice that the addition of 16 (10000 in binary) has caused the array to be reversed.

# To keep things simple (and to let you focus on the important part of this exercise), your function will receive its inputs as binary strings:

# >>> commands("00011")
# ["wink", "double blink"]


def commands(binary_str):
    dict = {4: "wink",
3: "double blink",
2: "close your eyes",
1: "jump",
0: "reverse"}
    z = [dict[i] for i, v in enumerate(binary_str) if v == '1']
    z.reverse()
    if "reverse" in z:
        z.remove("reverse")
        z.reverse()
    return z