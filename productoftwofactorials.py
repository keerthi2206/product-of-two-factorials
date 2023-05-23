def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num1 = int(input('enter your first number: '))
num2 = int(input('enter your second number: '))

factorial1 = factorial(num1)
factorial2 = factorial(num2)

result = factorial1 * factorial2
print(f"The product of {num1}! and {num2}! is: {result}")
