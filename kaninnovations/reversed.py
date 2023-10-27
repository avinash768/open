def reverse_integer(n):
    reversed_n = 0
    negative = n < 0  # Check if the input is negative
    
    if negative:
        n = -n  # Make it positive for the following operations
    
    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10

    return -reversed_n if negative else reversed_n

# Example usage:
n = 4312
reversed_n = reverse_integer(n)
print("Original:", n)
print("Reversed:", reversed_n)
