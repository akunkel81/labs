import time

# Memoization decorator
def memorize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

# Standard recursive Fibonacci
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

# Memoized Fibonacci
@memorize
def memorized_fibo(n):
    if n <= 1:
        return n
    else:
        return memorized_fibo(n - 1) + memorized_fibo(n - 2)


n = 35

start_time = time.time()
result_standard = recur_fibo(n)
time_standard = time.time() - start_time

start_time = time.time()
result_memoized = memorized_fibo(n)
time_memoized = time.time() - start_time

print(f"Standard Fibonacci result for n={n}: {result_standard}, Time: {time_standard:.6f} seconds")
print(f"Memoized Fibonacci result for n={n}: {result_memoized}, Time: {time_memoized:.6f} seconds")
