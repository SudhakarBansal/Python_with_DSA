# Rotate a List

# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_list(lst, k):
    if not lst:
        return []
    
    k = k % len(lst)  # Handle cases where k > len(lst)
    
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Add it at the front
    
    return lst


print(rotate_list([1, 2, 3, 4, 5],10))