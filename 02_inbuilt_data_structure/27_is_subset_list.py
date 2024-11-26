# Check if List is Subset of another List withouyt using "in" keyword

# Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
# Output: True

def is_subset(lst1, lst2):
    for item in lst1:
        found = False
        for x in lst2:
            if item == x:
                found = True
                break
        if not found:
            return False
    return True

print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
