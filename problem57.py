# Instructions
# Implement the classic method for composing secret messages called a square code.

# Given an English text, output the encoded version of that text.

# First, the input is normalized: the spaces and punctuation are removed from the English text and the message is downcased.

# Then, the normalized characters are broken into rows. These rows can be regarded as forming a rectangle when printed with intervening newlines.

# For example, the sentence

# "If man was meant to stay on the ground, god would have given us roots."
# is normalized to:

# "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
# The plaintext should be organized in to a rectangle. The size of the rectangle (r x c) should be decided by the length of the message, such that c >= r and c - r <= 1, where c is the number of columns and r is the number of rows.

# Our normalized text is 54 characters long, dictating a rectangle with c = 8 and r = 7:

# "ifmanwas"
# "meanttos"
# "tayonthe"
# "groundgo"
# "dwouldha"
# "vegivenu"
# "sroots  "
# The coded message is obtained by reading down the columns going left to right.

# The message above is coded as:

# "imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
# Output the encoded text in chunks that fill perfect rectangles (r X c), with c chunks of r length, separated by spaces. For phrases that are n characters short of the perfect rectangle, pad each of the last n chunks with a single trailing space.

# "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
# Notice that were we to stack these, we could visually decode the ciphertext back in to the original message:

# "imtgdvs"
# "fearwer"
# "mayoogo"
# "anouuio"
# "ntnnlvt"
# "wttddes"
# "aohghn "
# "sseoau "

def prepare_text_for_cypher(plain_text:str)->str:
    list_with_letters_of_clean_text = []
    list_with_letters_in_text = list(plain_text)

    for i in list_with_letters_in_text:
        if i.isalnum():
            list_with_letters_of_clean_text.append(i)
    return "".join(list_with_letters_of_clean_text).lower()

def columns_and_rows(plain_text):
    length_text = len(prepare_text_for_cypher(plain_text))

    for r in range(100000):
        for c in range(100000):
            if c-r <= 1 and c*r in range(length_text,length_text+c+1):
                return c,r
    
    
def from_normal_text_to_encoded(plain_text)->str:
    encoded_text = ""
    c,r= columns_and_rows(plain_text)
    if c == 0:
        return ""
    
    list_with_normal_text_split_on_cth_letter = [prepare_text_for_cypher(plain_text)[i:i+c] for i in range(0,len(prepare_text_for_cypher(plain_text)),c)]

    if len(list_with_normal_text_split_on_cth_letter[-1])<c:
        last_word_in_text = list_with_normal_text_split_on_cth_letter[-1]+ " "*(c-len(list_with_normal_text_split_on_cth_letter[-1]))
        list_with_normal_text_split_on_cth_letter[-1] = last_word_in_text
    
    for i in range(0,c):
        for j in range(0,len(list_with_normal_text_split_on_cth_letter)):
            encoded_text +=list_with_normal_text_split_on_cth_letter[j][i]

    return encoded_text.replace(" ","")

def cipher_text(plain_text):
    encoded_list = from_normal_text_to_encoded(plain_text)
    list_with_lengths_of_words = []
    cipher_text = []
    c,r = columns_and_rows(plain_text)
   
    length_of_cipher_text = len(from_normal_text_to_encoded(plain_text))
    final_word = ""
   
    while length_of_cipher_text>0:
        if c*r == len(from_normal_text_to_encoded(plain_text)):
            list_with_lengths_of_words.append(r)
        else:
            if length_of_cipher_text-r>=r-1:
                list_with_lengths_of_words.append(r)
            else:
                list_with_lengths_of_words.append(r-1)
        length_of_cipher_text-=r
    


    for i in list_with_lengths_of_words:
        if i == r:
            cipher_text.append(encoded_list[0:i])
        else:
            cipher_text.append(encoded_list[0:i]+" ")
        encoded_list = encoded_list[i:]


    for i in cipher_text:
        if len(cipher_text[-1])>2:
            if i != cipher_text[-1]:
                final_word +=i + " "
            else:
                final_word +=i
        else:
            return "".join(cipher_text)
  
    return final_word
    
print(cipher_text("A"))



