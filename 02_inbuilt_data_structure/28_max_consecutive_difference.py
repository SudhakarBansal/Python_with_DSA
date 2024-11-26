# Maximum difference between two consecutive elements in a list.

def max_consecutive_difference(lst):
    if len(lst) < 2:  # Handle edge case for empty or single-element list
        return 0
    
    n= len(lst)-1
    max_diff =0
    for i in range(0,n):
        diff = abs(lst[i]-lst[i+1])    
        if max_diff < diff:
            max_diff = diff
    return max_diff


print(max_consecutive_difference([28]))