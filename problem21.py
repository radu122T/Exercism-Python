# Instructions
# Given a word, compute the Scrabble score for that word.

# Letter Values
# You'll need these:

# Letter                           Value
# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10
# Examples
# "cabbage" should be scored as worth 14 points:

# 3 points for C
# 1 point for A, twice
# 3 points for B, twice
# 2 points for G
# 1 point for E
# And to total:

# 3 + 2*1 + 2*3 + 2 + 1
# = 3 + 2 + 6 + 3
# = 5 + 9
# = 14
# Extensions
# You can play a double or a triple letter.
# You can play a double or a triple word.

def score(word):
    count = 0
    letters = dict()
    letters[1] = ["A","E","I","O","U","L","N","R","S","T"]
    letters[2] = ["D","G"]                               
    letters[3] = ["B","C","M","P"]
    letters[4] = ["F","H","V","W","Y"]
    letters[5] = ["K"]
    letters[8] = ["J","X"]
    letters[10] = ["Q","Z"]
    
    for i in word.upper():
        for k in letters.keys():
            if i in letters[k]:
                count += k
                
    return count