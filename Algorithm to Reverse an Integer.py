def reverse_an_integer(number):
    number = str(number)
    # Converts number to an string so that I can complete operations on it
    number = list(number)
    # Converts string to a list
    number.reverse()
    # Reverse the order of the list so I can have reversed integer
    number = "".join(number)
    # Use join method to turn the reversed list back into a string
    number = int(number)
    # Converts the number back into an integer
    # This is done in one inputs 200
    # 200 reversed is 002
    # 002 is the same as 2
    return number
    # I can now return my reversed integer

reverse_an_integer(76)
