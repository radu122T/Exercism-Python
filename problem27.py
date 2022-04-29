# Instructions
# Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once. The best known English pangram is:

# The quick brown fox jumps over the lazy dog.

# The alphabet used consists of ASCII letters a to z, inclusive, and is case insensitive. Input will not contain non-ASCII symbols.

import string
def is_pangram(sentence):
    sentence = [i.lower() for i in sentence if i.isalpha()]
    dict_with_letters_and_values_0 = {i:0 for i in string.ascii_lowercase}
    for letter in sentence:
        for value in dict_with_letters_and_values_0.keys():
            if letter == value:
                dict_with_letters_and_values_0[letter]+= 1
    print(dict_with_letters_and_values_0)
    for value in dict_with_letters_and_values_0.values():
        print(value)
        if value == 0:
            return False
    return True