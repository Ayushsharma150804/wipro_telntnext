# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except Exception as e:
    print("Error:", e)
else:
    print("Result:", result)


# Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    n = int(input("Enter a number: "))
    if n <= 1:
        print(f"{n} is not a prime number")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
except ValueError:
    print("Error: Please enter a valid number")


# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
filename = input("Enter file name: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
    print(content.title())
except FileNotFoundError:
    print("Error: File not found")


# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
lst = [5, -3, 7, 0, -1, 8, -6, 2, -4, 9]
try:
    idx = int(input("Enter an index (0-9): "))
    num = lst[idx]
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
except IndexError:
    print("Error: Invalid index")
except ValueError:
    print("Error: Please enter a valid integer index")
