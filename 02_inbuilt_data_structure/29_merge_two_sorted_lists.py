# Merge two Sorted List

# Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

def merge_two_sorted_lists(list1, list2):
    i, j = 0, 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Append remaining elements, if any
    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

print(merge_two_sorted_lists([2,3,5,8],[1,4,7]))