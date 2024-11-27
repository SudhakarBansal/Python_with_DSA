# Merge 2 List into Dictionary

# Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

def merge_lists_to_dictionary(keys, values):
    # Boundary condition: Ensure both lists are of equal length
    lkeys = len(keys)
    if lkeys != len(values):
        return False
    
    # Create the dictionary
    result = {}
    for i in range(lkeys):
        result[keys[i]] = values[i]
    
    return result

print(merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2, 3]))



# pythonic way:

# def merge_lists_to_dictionary(keys, values):
#     if len(keys) != len(values):
#         return False
#     return dict(zip(keys, values))

# print(merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2, 3]))
