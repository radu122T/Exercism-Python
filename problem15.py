# Manage a game player's High Score list.

# Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

# In this exercise, you're going to use and manipulate lists. Python lists are very versatile, and you'll find yourself using them again and again in problems both simple and complex.

# Data Structures (Python 3 Documentation Tutorial)
# Lists and Tuples in Python (Real Python)
# Python Lists (Google for Education)


def latest(scores):
   return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    x = sorted(scores)
    y = x[-3:]
    y.reverse()
    return y
    