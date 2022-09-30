# This file is for basic functions.

# This function will convert a string into a float.
# First, It will check if the string is empty, if so return null.
# Otherwise, convert incoming string into float, then return the float as
# an integer instead. As converting the string directly into an int doesn't
# always work with some values in the dataset.

def str_convert(incoming_str):
    if incoming_str == '':
        return None
    else:
        str_float = float(incoming_str)
        return int(str_float)
