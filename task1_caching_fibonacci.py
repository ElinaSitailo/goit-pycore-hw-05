def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            result = cache[n]
            print(f"Fetching from cache for: {n}, {result}")
            return result
        if n <= 1:
            return n

        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        print(f"Save to cache for: {n}, {result}")
        return result

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    i = 10
    result = fib(i)
    print(f"-----Fibonacci of {i} is: {result}\n")

    i = 15
    result = fib(i)
    print(f"-----Fibonacci of {i} is: {result}\n")

    i = 10
    result = fib(i)
    print(f"-----Fibonacci of {i} is: {result}\n")

    assert fib(10) == (55)
    assert fib(15) == (610)
