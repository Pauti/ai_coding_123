def fibonacci(n):
    result = 0
    a, b = 0, 1
    for i in range(n + 1):
        result = a
        a, b = b, a + b
        print(f'{i}: {result}')
    return result

fibonacci(10)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial: " + str(factorial(5)))