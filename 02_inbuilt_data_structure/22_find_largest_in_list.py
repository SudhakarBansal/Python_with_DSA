#Largest Element in a List

# Input: numbers = [3, 8, 2, 10, 5]
# Output: 10

def find_largest(numbers):
    max = numbers[0]
    for i in range(len(numbers)-1):
        if numbers[i]<numbers[i+1]:
            max=numbers[i+1]
    return(max)   

print(find_largest([-5, -10, -2, -1, -7]))