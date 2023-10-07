def max_key_in_dict(my_dict):
    my_dict = dict(my_dict)
    keymax = max(my_dict, key = my_dict.get)
    return keymax



