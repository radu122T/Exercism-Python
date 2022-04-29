# Instructions
# Azara and Rui are teammates competing in a pirate-themed treasure hunt. One has a list of treasures with map coordinates, the other a list of location names with map coordinates. They've also been given blank maps with a starting place marked YOU ARE HERE.


# Azara's List		Rui's List
# Treasure	Coordinates
# Amethyst Octopus	1F
# Angry Monkey Figurine	5B
# Antique Glass Fishnet Float	3D
# Brass Spyglass	4B
# Carved Wooden Elephant	8C
# Crystal Crab	6A
# Glass Starfish	6D
# Model Ship in Large Bottle	8A
# Pirate Flag	7F
# Robot Parrot	1C
# Scrimshaw Whale's Tooth	2A
# Silver Seahorse	4E
# Vintage Pirate Hat	7E		
# Location Name	Coordinates	Quandrant
# Seaside Cottages	("1", "C")	Blue
# Aqua Lagoon (Island of Mystery)	("1", "F")	Yellow
# Deserted Docks	("2", "A")	Blue
# Spiky Rocks	("3", "D")	Yellow
# Abandoned Lighthouse	("4", "B")	Blue
# Hidden Spring (Island of Mystery)	("4", "E")	Yellow
# Stormy Breakwater	("5", "B")	Purple
# Old Schooner	("6", "A")	Purple
# Tangled Seaweed Patch	("6", "D")	Orange
# Quiet Inlet (Island of Mystery)	("7", "E")	Orange
# Windswept Hilltop (Island of Mystery)	("7", "F")	Orange
# Harbor Managers Office	("8", "A")	Purple
# Foggy Seacave	("8", "C")	Purple

# But things are a bit disorganized: Azara's coordinates appear to be formatted and sorted differently from Rui's, and they have to keep looking from one list to the other to figure out which treasures go with which locations. Being budding pythonistas, they have come to you for help in writing a small program (a set of functions, really) to better organize their hunt information.

# 1. Extract coordinates
# Implement the get_coordinate() function that takes a (treasure, coordinate) pair from Azara's list and returns only the extracted map coordinate.

# >>> get_coordinate(("Scrimshaw Whale's Tooth", "2A"))
# "2A"
# 2. Format coordinates
# Implement the convert_coordinate() function that takes a coordinate in the format "2A" and returns a tuple in the format ("2", "A").

# >>> convert_coordinate("2A")
# ("2", "A")
# 3. Match coordinates
# Implement the compare_records() function that takes a (treasure, coordinate) pair and a (location, coordinate, quadrant) record and compares coordinates from each. Return True if the coordinates "match", and return False if they do not. Re-format coordinates as needed for accurate comparison.

# >>> compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
# False

# >>> compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))
# True
# 4. Combine matched records
# Implement the create_record() function that takes a (treasure, coordinate) pair from Azara's list and a (location, coordinate, quadrant) record from Rui's list and returns (treasure, coordinate, location, coordinate, quadrant) if the coordinates match. If the coordinates do not match, return the string "not a match". Re-format the coordinate as needed for accurate comparison.

# >>> create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
# ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

# >>> create_record(('Brass Spyglass', '4B'), (('1', 'C'), 'Seaside Cottages', 'blue'))
# "not a match"
# 5. "Clean up" & make a report of all records
# Clean up the combined records from Azara and Rui so that there's only one set of coordinates per record. Make a report so they can see one list of everything they need to put on their maps. Implement the clean_up() function that takes a tuple of tuples (everything from both lists), looping through the outer tuple, dropping the unwanted coordinates from each inner tuple and adding each to a 'report'. Format and return the 'report' so that there is one cleaned record on each line.

# >>> clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))

# """
# ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
# ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
# ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
# """

def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    list1 = []
    for i in coordinate:
        list1.append(i)
        x = tuple(list1)
    return x


def compare_records(azara_record, rui_record):
    x = []
    azara = list(azara_record)
    for i in azara[1]:
        x.append(i)
    return tuple(x) == rui_record[1]
    
def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record 
    else:
        return "not a match"
    


def clean_up(combined_record_group):
    return "".join([f"{(record[0], record[2], record[3], record[4])}\n" for record in combined_record_group])

        
            
    
 