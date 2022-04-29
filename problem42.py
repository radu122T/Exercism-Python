# Instructions
# Add the mine counts to a completed Minesweeper board.

# Minesweeper is a popular game where the user has to find the mines using numeric hints that indicate how many mines are directly adjacent (horizontally, vertically, diagonally) to a square.

# In this exercise you have to create some code that counts the number of mines adjacent to a given empty square and replaces that square with the count.

# The board is a rectangle composed of blank space (' ') characters. A mine is represented by an asterisk ('*') character.

# If a given space has no adjacent mines at all, leave that square blank.

# Examples
# For example you may receive a 5 x 4 board like this (empty spaces are represented here with the '·' character for display on screen):

# ·*·*·
# ··*··
# ··*··
# ·····
# And your code will transform it into this:

# 1*3*1
# 13*31
# ·2*2·
# ·111·
# Exception messages
# Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

# This particular exercise requires that you use the raise statement to "throw" a ValueError when the board() function receives malformed input. The tests will only pass if you both raise the exception and include a message with it.

# To raise a ValueError with a message, write the message as an argument to the exception type:

# # when the board receives malformed input
# raise ValueError("The board is invalid with current input.")

def annotate(minefield):
    
    if not all(len(i) == len(minefield[0]) for i in minefield):
        raise ValueError("The board is invalid with current input.")
    result = []
    for y, line in enumerate(minefield):
        temp = ""
        for x, char in enumerate(line):
            if char == " ":
                temp += str(count_position(minefield, x, y))
            elif char == "*":
                temp += char
            else:
                raise ValueError("The board is invalid with current input.")
        result.append(temp)
    return result
def count_position(minefield: list, x: int, y: int):
    x1 = max(x-1, 0)
    y1 = max(y-1, 0)
    x2 = min(x+1, len(minefield[y]))
    y2 = min(y+1, len(minefield))
    result = str("".join([x[x1:x2+1] for x in minefield[y1:y2+1]]).count("*"))
    if result == "0":
        result = " "
    return result
