# Write a function to return the sum of all numbers in a list.  
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def sum_of_list(numbers):
    return sum(numbers)


# Write a function to return the reverse of a string.  
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def reverse_string(s):
    return s[::-1]


# Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 
def count_upper_lower(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    print("Upper case letters:", upper_count)
    print("Lower case letters:", lower_count)


# Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def print_even_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    print(evens)


# Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
