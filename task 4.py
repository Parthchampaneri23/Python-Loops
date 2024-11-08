#Python program to get the Fibonacci series between 0 to 50


def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        if a <= 50:
            result.append(a)
            a, b = b, a + b
    return result

print(fibonacci(50))
