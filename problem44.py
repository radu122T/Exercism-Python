# Instructions
# Implement a binary search algorithm.

# Searching a sorted collection is a common task. A dictionary is a sorted list of word definitions. Given a word, one can find its definition. A telephone book is a sorted list of people's names, addresses, and telephone numbers. Knowing someone's name allows one to quickly find their telephone number and address.

# If the list to be searched contains more than a few items (a dozen, say) a binary search will require far fewer comparisons than a linear search, but it imposes the requirement that the list be sorted.

# In computer science, a binary search or half-interval search algorithm finds the position of a specified input value (the search "key") within an array sorted by key value.

# In each step, the algorithm compares the search key value with the key value of the middle element of the array.

# If the keys match, then a matching element has been found and its index, or position, is returned.

# Otherwise, if the search key is less than the middle element's key, then the algorithm repeats its action on the sub-array to the left of the middle element or, if the search key is greater, on the sub-array to the right.

# If the remaining array to be searched is empty, then the key cannot be found in the array and a special "not found" indication is returned.

# A binary search halves the number of items to check with each iteration, so locating an item (or determining its absence) takes logarithmic time. A binary search is a dichotomic divide and conquer search algorithm.

# Exception messages
# Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

# This particular exercise requires that you use the raise statement to "throw" a ValueError when the given value is not found within the array. The tests will only pass if you both raise the exception and include a message with it.

# To raise a ValueError with a message, write the message as an argument to the exception type:

# # example when value is not found in the array.
# raise ValueError("value not in array")


def find(search_list, value):
    if search_list:
        mid = len(search_list)//2
    else:
        raise ValueError("value not in array")
    if search_list[mid] == value:
        return mid
    elif search_list[mid]!= value and mid == 0:
        return -1000000

    search_list_right = search_list[mid+1:]
    search_list_left = search_list[:mid]

    if search_list[mid] > value:
        if find(search_list_left, value)<0 or search_list_left == []: 
            raise ValueError ("value not in array") 
        return find(search_list_left, value)
    else:
        if mid + 1 + find(search_list_right, value)<0 or search_list_right == []:
            raise ValueError("value not in array")
        else: 
            return mid + 1 +find(search_list_right, value)