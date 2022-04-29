# Instructions
# Implement basic list operations.

# In functional languages list operations like length, map, and reduce are very common. Implement a series of basic list operations, without using existing functions.

# The precise number and names of the operations to be implemented will be track dependent to avoid conflicts with existing names, but the general operations you will implement include:

# append (given two lists, add all items in the second list to the end of the first list);
# concatenate (given a series of lists, combine all items in all lists into one flattened list);
# filter (given a predicate and a list, return the list of all items for which predicate(item) is True);
# length (given a list, return the total number of items within it);
# map (given a function and a list, return the list of the results of applying function(item) on all items);
# foldl (given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left using function(accumulator, item));
# foldr (given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right using function(item, accumulator));
# reverse (given a list, return a list with all the original items, but in reversed order);

def append(list1, list2):
    list1 = list1 + list2
    return list1


def concat(lists):
    k = [item for sublist in lists for item in sublist]
    return k

def filter(function, list):
    k = []
    for i in list:
        if function(i):
            k.append(i)
    return k



def length(list):
    counter = 0
    for i in list:
        counter +=1
    return counter


def map(function, list):
    k = []
    for i in list:
        k.append(function(i))
    return k


def foldl(function, list, initial):
    it = iter(list)
    value = initial
    for element in it:
        value = function(value, element)
    return value



def foldr(function, iterable, initializer):
    result = initializer
    for item in reverse(iterable):
        result = function(item, result)
    return result


def reverse(lists):
    return lists[::-1]
