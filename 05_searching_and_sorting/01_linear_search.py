def linear_search(arr, target):
    # TODO: Implement this function
    size = len(arr)
    for i in range(0,size):
        if arr[i]==target:
            return i
    return -1

print(linear_search([3, 7, 2, 5], 5) )