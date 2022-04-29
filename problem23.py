# Instructions
# Given a diagram, determine which plants each child in the kindergarten class is responsible for.

# The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, plant them in actual dirt, and grow actual plants.

# They've chosen to grow grass, clover, radishes, and violets.

# To this end, the children have put little cups along the window sills, and planted one type of plant in each cup, choosing randomly from the available types of seeds.

# [window][window][window]
# ........................ # each dot represents a cup
# ........................
# There are 12 children in the class:

# Alice, Bob, Charlie, David,
# Eve, Fred, Ginny, Harriet,
# Ileana, Joseph, Kincaid, and Larry.
# Each child gets 4 cups, two on each row. Their teacher assigns cups to the children alphabetically by their names.

# The following diagram represents Alice's plants:

# [window][window][window]
# VR......................
# RG......................
# In the first row, nearest the windows, she has a violet and a radish. In the second row she has a radish and some grass.

# Your program will be given the plants from left-to-right starting with the row nearest the windows. From this, it should be able to determine which plants belong to each student.

# For example, if it's told that the garden looks like so:

# [window][window][window]
# VRCGVVRVCGGCCGVRGCVCGCGV
# VRCCCGCRRGVCGCRVVCVGCGCV
# Then if asked for Alice's plants, it should provide:

# Violets, radishes, violets, radishes
# While asking for Bob's plants would yield:

# Clover, grass, clover, clover

plants = {
"V": "Violets",
"R": "Radishes",
"C": "Clover",
"G": "Grass"}

class Garden:
    people_and_plants = {
"Alice":0,
"Bob" : 2,
"Charlie" : 4,
"David" : 6,
"Eve" : 8,
"Fred" : 10,
"Ginny" : 12,
"Harriet" : 14,
"Ileana"  : 16,
"Joseph" : 18,
"Kincaid" : 20,
"Larry" : 22}
    def __init__(self, diagram, students=None):
        self.students = students
        self.final_plants_list = []
        self.final_plants_list2= []
        self.diagram = [list(word) for word in diagram.splitlines()]
        self.plants_first_row_full_name = [plants[i] for i in self.diagram[0]]
        self.plants_second_row_full_name = [plants[i] for i in self.diagram[1]]
        if self.students != None:
            self.students = sorted(students)
            Garden.people_and_plants = {self.students[i] : i*2 for i in range(0,len(self.students))}

    def plants(self, name):
        self.final_plants_list.extend(self.plants_first_row_full_name[Garden.people_and_plants[name]:Garden.people_and_plants[name]+2])
        self.final_plants_list2.extend(self.plants_second_row_full_name[Garden.people_and_plants[name]:Garden.people_and_plants[name]+2])
        self.final_plants_list.extend(self.final_plants_list2)
        return self.final_plants_list

        