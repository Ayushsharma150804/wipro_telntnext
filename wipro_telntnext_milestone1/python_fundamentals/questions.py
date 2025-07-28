# 1. Write a program to check if a given number is Positive, Negative, or Zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Write a program to check if a given number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Given two non-negative values, print true if they have the same last digit.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a % 10 == b % 10:
    print("True")
else:
    print("False")

# 4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end="\t")
print()

# 5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# 6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# 7. Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# 8. Write a program to print the sum of all the digits of a given number.
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)

# 9. Write a program to reverse a given number and print.
num = int(input("Enter a number: "))
reverse = 0
original = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

# 10. Write a program to find if the given number is palindrome or not.
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
