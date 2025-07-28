# Write a program to accept two numbers as command line arguments and display their sum.
import sys

if len(sys.argv) >= 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)
else:
    print("Please provide two numbers as command line arguments.")


# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys

if len(sys.argv) >= 2:
    welcome_message = " ".join(sys.argv[1:])
    print(f"File name: {sys.argv[0]}")
    print("Welcome message:", welcome_message)
else:
    print("Please provide a welcome message as command line arguments.")


# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if len(sys.argv) >= 11:
    numbers = list(map(int, sys.argv[1:11]))
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
else:
    print("Please provide 10 numbers as command line arguments.")
