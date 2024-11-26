#Count Number of Odd and Even Elements in a List

# Input: lst = [1, 2, 3, 4, 5]
# Output: (2, 3)

def count_even_odd(lst):
    even =odd= 0
    for item in lst:
        if item%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

print(count_even_odd([1, 2, 3, 4, 5]))