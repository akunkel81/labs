def product_of_digits(x):
    # Use absolute value to handle negative numbers
    x = abs(x)
    # Base case: if x is a single digit, return x
    if x < 10:
        return x
    # Recursive case: multiply the last digit by the product of the rest
    return (x % 10) * product_of_digits(x // 10)

# Examples
print(product_of_digits(234))  # Output: 24
print(product_of_digits(12))   # Output: 2
print(product_of_digits(-12))  # Output: 2

def array_to_string(a, index=0):
    # Base case: when index reaches the last element
    if index == len(a) - 1:
        return str(a[index])
    # Recursive case: add current element and recurse for the rest
    return str(a[index]) + "," + array_to_string(a, index + 1)

# Examples
print(array_to_string([1, 2, 3, 4]))  # Output: "1,2,3,4"
print(array_to_string([10, 20, 30]))  # Output: "10,20,30"

def log(base, value, count=0):
    # Check for valid inputs
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1.")
    # Base case: if value is less than the base, return the count
    if value < base:
        return count
    # Recursive case: divide value by base and increase count
    return log(base, value // base, count + 1)

# Examples
print(log(10, 123456))  # Output: 5
print(log(2, 64))       # Output: 6
print(log(10, 4567))    # Output: 3
