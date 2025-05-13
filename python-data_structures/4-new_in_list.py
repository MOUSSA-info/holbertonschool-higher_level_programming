def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    # Create a copy of the list
    new_list = my_list[:]
    # Replace the element at the specified index
    new_list[idx] = element
    return new_list
