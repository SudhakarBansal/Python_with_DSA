# Check if all elements in a list are Unique

def check_unique(lst):
    seen= set()

    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

print(check_unique([1, 2, 3, 4,2, 5]))
