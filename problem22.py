# Instructions
# Convert a phrase to its acronym.

# Techies love their TLA (Three Letter Acronyms)!

# Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).

def abbreviate(words):
    y = words.upper().replace("-"," ").replace("_","").split()
    z = "".join([y[i][0] for i in range(len(y))])
    return z
    