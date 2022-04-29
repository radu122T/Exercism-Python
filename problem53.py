# Instructions
# Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.

# The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. The first letter is replaced with the last letter, the second with the second-last, and so on.

# An Atbash cipher for the Latin alphabet would be as follows:

# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: zyxwvutsrqponmlkjihgfedcba
# It is a very weak cipher because it only has one possible key, and it is a simple monoalphabetic substitution cipher. However, this may not have been an issue in the cipher's time.

# Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, and punctuation is excluded. This is to make it harder to guess things based on word boundaries.

# Examples
# Encoding test gives gvhg
# Decoding gvhg gives test
# Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog


from textwrap import wrap
plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"
dict = {plain_letter:cipher_letter for plain_letter,cipher_letter in zip(list(plain),list(cipher))}
def encode(plain_text):
    list_with_plain_text = []
    list_with_encoded_text = []
    
    for letter in plain_text:
        if letter.isalnum():
            list_with_plain_text.append(letter.lower())
    
    for item in list_with_plain_text:
        if item.isalpha():
            item = dict[item]
            list_with_encoded_text.append(item)
        else:
            list_with_encoded_text.append(item)
    final_word = "".join(list_with_encoded_text)
    
    return " ".join(wrap(final_word,5))
    
def decode(ciphered_text):
    return encode(ciphered_text).replace(" ","")
