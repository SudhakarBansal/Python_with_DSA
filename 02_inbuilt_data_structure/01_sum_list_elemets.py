# Sum of List Elements

# Input: numbers = [1, 2, 3, 4, 5]
# Output: 15

def sum_list(numbers):
    # Your code goes here
    sum = 0
    for i in range(len(numbers)):
        sum+= numbers[i]
    return sum    
        
print(sum_list([1, 2, 3, 4, 5]))