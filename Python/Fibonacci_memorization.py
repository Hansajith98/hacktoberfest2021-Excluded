# Improved Fibonacci sequence with memorization
def fibonacci(n, fibonacci_cache={}):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    elif n == 0:
        return 0
    elif n > 0 and n <= 2:
        return 1
    else:
        fibonacci_cache[n] = fibonacci(n - 1, fibonacci_cache) + fibonacci(n - 2, fibonacci_cache)
        return fibonacci_cache[n]
