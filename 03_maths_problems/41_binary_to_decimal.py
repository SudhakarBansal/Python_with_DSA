def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    isnegative = binary_str[0] == "-"  # Check if the binary number is negative
    if isnegative:
        binary_str = binary_str[1:]  # Remove the negative sign

    result = 0
    power_of_two = 1  # Start with 2^0

    # Traverse the binary string in reverse
    for digit in reversed(binary_str):
        if digit == "1":
            result += power_of_two
        power_of_two *= 2  # Increment power of 2 for the next digit

    if isnegative:
        result *= -1  # Apply negative sign if needed

    return result


# Test cases
print(binary_to_decimal("-111"))  # Output: -7
print(binary_to_decimal("101"))   # Output: 5
print(binary_to_decimal("0"))     # Output: 0
