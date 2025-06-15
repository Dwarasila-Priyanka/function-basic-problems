# 1. write aa function to square a number
def square(n):
    return n * n

result = square(4)
print("Square:", result)

#2.Add two numbers using function
def add(a, b):
    return a + b

print("Sum:", add(10, 5))

#3.Check even or odd
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # True
print(is_even(7))  # False

#4. Maximum of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(10, 5, 7))

#5. Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # 120

#6. Palindrome checker
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
