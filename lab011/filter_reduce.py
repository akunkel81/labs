from functools import reduce

def custom_filter(func, iterable):
    return reduce(
        lambda acc, x: acc + [x] if func(x) else acc,
        iterable,
        []
    )

# Examples
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(custom_filter(lambda x: x % 2 == 0, numbers))  # Filters even numbers
