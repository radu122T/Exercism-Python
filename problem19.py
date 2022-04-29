# Instructions
# Output the lyrics to 'The Twelve Days of Christmas'.

# On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

# On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

# On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.


GIFTS = dict()
GIFTS[1] = "a Partridge in a Pear Tree"
GIFTS[2] = "two Turtle Doves"
GIFTS[3] = "three French Hens"
GIFTS[4] = "four Calling Birds"
GIFTS[5] = "five Gold Rings"
GIFTS[6] = "six Geese-a-Laying"
GIFTS[7] = "seven Swans-a-Swimming"
GIFTS[8] = "eight Maids-a-Milking"
GIFTS[9] = "nine Ladies Dancing"
GIFTS[10] = "ten Lords-a-Leaping"
GIFTS[11] = "eleven Pipers Piping"
GIFTS[12] = "twelve Drummers Drumming"
DAYS = ["zeroth", "first", "second", "third", "fourth", "fifth",  "sixth", "seventh", "eighth", "ninth", "tenth",             "eleventh", "twelfth"]

def recite(start_verse, end_verse):
    lyrics = []
    for day in range(start_verse, end_verse + 1):
        verse = f"On the {DAYS[day]} day of Christmas my true love gave to me: "
        for gift in range(day, 0, -1):
            verse = verse + ("and " if (gift == 1 and day > 1) else "")
            verse = verse + GIFTS[gift]
            verse = verse + ("." if gift == 1 else ", ")
        lyrics.append(verse)
    return lyrics
