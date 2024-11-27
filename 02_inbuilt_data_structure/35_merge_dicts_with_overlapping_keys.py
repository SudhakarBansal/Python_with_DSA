# Merge Dictionaries with Common Keys

# Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
# Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}

def merge_dicts_with_overlapping_keys(dicts:list[dict])->dict:
    result_dct ={}
    for inner_dict in dicts:
        for key,value in inner_dict.items():
            if key in result_dct:
                result_dct[key]+=value
            else:
                result_dct[key]=value
    return result_dct

print(merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))

