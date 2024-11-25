# Remove Duplicate in a List

# Input: lst = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

def remove_duplicates(lst):
    unq_lst=[]
    for item in lst:
       if item not in unq_lst:
           unq_lst.append(item)
    return unq_lst
    
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))