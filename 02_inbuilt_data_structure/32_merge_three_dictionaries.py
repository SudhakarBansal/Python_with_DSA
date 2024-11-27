# Merge Multiple Dictionaries

# Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

def merge_three_dictionaries(dict1, dict2, dict3):
    dct ={}
    for x, y in dict1.items():
        dct[x]=y
    for x, y in dict2.items():
        dct[x]=y
    for x, y in dict3.items():
        dct[x]=y
    return dct
print(merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))



# pythonic ways - 1:
# def merge_three_dictionaries(dict1, dict2, dict3):
#     return {**dict1, **dict2, **dict3}

# print(merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))


# pythonic ways - 2:
# def merge_three_dictionaries(dict1, dict2, dict3):
#     result = {}
#     result.update(dict1)
#     result.update(dict2)
#     result.update(dict3)
#     return result

# print(merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))


# pythonic ways - 3:
# def merge_multiple_dictionaries(*dicts):
#     result = {}
#     for d in dicts:
#         result.update(d)
#     return result

# print(merge_multiple_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))
