def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


try:
    num = int(input("Enter Number for factorial: "))
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    print(f'Factorial of {num} is {factorial(num)}')
except ValueError as e:
    print(f'Error: {e}')
