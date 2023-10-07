def remove_duplicates_from_list(list_of_nums):
    set_of_nums = set(list_of_nums)
    # Change list to set
    # Sets remove duplicates
    new_list_of_nums = list(set_of_nums)
    # Change set back to list
    x = len(new_list_of_nums)
    # Assign variable to length of the new list
    return x
    # Return the new value

remove_duplicates_from_list([6, 7, 8, 7, 6, 5, 4, 3, 2, 1, 10])

