# Instructions
# An anagram is a rearrangement of letters to form a new word. Given a word and a list of candidates, select the sublist of anagrams of the given word.

# Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".

def find_anagrams(word, candidates):
    x = []
    for i in candidates:
        if i.upper() != word.upper() and sorted(list(i.upper()))==sorted(list(word.upper())):
            x.append(i)
    return x