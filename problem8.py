# Instructions
# Chaitana owns a very popular theme park. She only has one ride in the very center of beautifully landscaped grounds: The Biggest Roller Coaster in the World(TM). Although there is only this one attraction, people travel from all over the world and stand in line for hours for the opportunity to ride Chaitana's hypercoaster.

# There are two queues for this ride, each represented as a list:

# Normal Queue
# Express Queue (also known as the Fast-track) - where people pay extra for priority access.
# You have been asked to write some code to better manage the guests at the park. You need to implement the following functions as soon as possible before the guests (and your boss, Chaitana!) get cranky.

# 1. Add me to the queue
# Define the add_me_to_the_queue() function that takes 4 parameters <express_queue>, <normal_queue>, <ticket_type>, <person_name> and returns the appropriate queue updated with the person's name.

# <ticket_type> is an int with 1 == express_queue and 0 == normal_queue.
# <person_name> is the name (as a str) of the person to be added to the respective queue.
# >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")
# ...
# ["Tony", "Bruce", "RichieRich"]

# >>> add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye")
# ....
# ["RobotGuy", "WW", "HawkEye"]
# 2. Where are my friends?
# One person arrived late at the park but wants to join the queue where their friends are waiting. But they have no idea where their friends are standing and there isn't any phone reception to call them.

# Define the find_my_friend() function that takes 2 parameters queue and friend_name and returns the position in the queue of the person's name.

# <queue> is the list of people standing in the queue.
# <friend_name> is the name of the friend whose index (place in the queue) you need to find.
# Remember: Indexing starts at 0 from the left, and -1 from the right.

# >>> find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve")
# ...
# 1
# 3. Can I please join them?
# Now that their friends have been found (in task #2 above), the late arriver would like to join them at their place in the queue. Define the add_me_with_my_friends() function that takes 3 parameters queue, index, and person_name.

# <queue> is the list of people standing in the queue.
# <index> is the position at which the new person should be added.
# <person_name> is the name of the person to add at the index position.
# Return the queue updated with the late arrivals name.

# >>> add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")
# ...
# ["Natasha", "Bucky", "Steve", "T'challa", "Wanda", "Rocket"]
# 4. Mean person in the queue
# You just heard from the queue that there is a really mean person shoving, shouting, and making trouble. You need to throw that miscreant out for bad behavior!

# Define the remove_the_mean_person() function that takes 2 parameters queue and person_name.

# <queue> is the list of people standing in the queue.
# <person_name> is the name of the person that needs to be kicked out.
# Return the queue updated without the mean person's name.

# >>> remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
# ...
# ["Natasha", "Steve", "Wanda", "Rocket"]
# 5. Namefellows
# You may not have seen two unrelated people who look exactly the same, but you have definitely seen unrelated people with the exact same name (namefellows)! Today, it looks like there are a lot of them in attendance. You want to know how many times a particular name occurs in the queue.

# Define the how_many_namefellows() function that takes 2 parameters queue and person_name.

# <queue> is the list of people standing in the queue.
# <person_name> is the name you think might occur more than once in the queue.
# Return the number of occurrences of person_name, as an int.

# >>> how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
# ...
# 2
# 6. Remove the last person
# Sadly, it's overcrowded at the park today and you need to remove the last person in the normal line (you will give them a voucher to come back in the fast-track on another day). You will have to define the function remove_the_last_person() that takes 1 parameter queue, which is the list of people standing in the queue.

# You should update the list and also return the name of the person who was removed, so you can write them a voucher.

# >>> remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
# ...
# 'Rocket'
# 7. Sort the Queue List
# For administrative purposes, you need to get all the names in a given queue in alphabetical order.

# Define the sorted_names() function that takes 1 argument, queue, (the list of people standing in the queue), and returns a sorted copy of the list.

# >>> sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
# ...
# ['Eltran', 'Natasha', 'Natasha', 'Rocket', 'Steve']


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    new_list = [person_name]
    if ticket_type:
        express_queue.extend(new_list)
        return express_queue
    normal_queue.extend(new_list)
    return normal_queue

def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index,person_name)
    return queue
    
def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    x=queue.count(person_name)
    return x

def remove_the_last_person(queue):
    x = queue[-1]
    queue.pop()
    return x

def sorted_names(queue):
    x = sorted(queue)