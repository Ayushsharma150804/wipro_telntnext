# 1. Write a program to count the number of upper and lower case letters in a String.
input_str = "Hello World!"
upper_count = 0
lower_count = 0
for char in input_str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

# 2. Write a program that will check whether a given String is Palindrome or not.
palindrome_str = "madam"
if palindrome_str == palindrome_str[::-1]:
    print(f"'{palindrome_str}' is a palindrome.")
else:
    print(f"'{palindrome_str}' is not a palindrome.")

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string 
# where n is the length of the string. The string length will be >=2.
# If input is "Wipro" then output should be "WiWiWiWiWi".
original_str = "Wipro"
n = len(original_str)
first_two = original_str[:2]
result = first_two * n
print("Resulting string:", result)

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' characters,
# else return the string unchanged. If the input is "xHix", then output is "Hi".
test_str = "xHix"
if test_str.startswith('x'):
    test_str = test_str[1:]
if test_str.endswith('x'):
    test_str = test_str[:-1]
print("Modified string:", test_str)

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
main_str = "Wipro"
n = 3
last_n = main_str[-n:]
result = last_n * n
print("Repeated last n chars:", result)

