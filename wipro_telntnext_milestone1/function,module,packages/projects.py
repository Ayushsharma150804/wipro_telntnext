# Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
#
# Constraint: All the colors will be completely in either lower case or upper case.
#
# Sample input 1: green-red-yellow-black-white
# Sample output 1: black-green-red-white-yellow
#
# Sample input 2: PINK-BLUE-TAN-PURPLE
# Sample output 2: BLUE-PINK-PURPLE-TAN

def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)


# Create a Python module with the following functions:
#
# Function Name: Tusk
#
# Ispalindrome(name)
# Given the user name as input, this function should tell us whether the name is a palindrome or not.
#
# count_the_vowels(name)
# Given the user name as input, this function should tell us how many vowels are present in it.
#
# frequency_of_letters(name)
# Given the user name as input, this function should tell us how many times each letter appears in the name.
#
# Note: name will be completely in either lower case or upper case.

def Ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in name if char in vowels)
    print("No of vowels:", count)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != ' ':  # ignoring spaces
            freq[char] = freq.get(char, 0) + 1
    freq_str = ', '.join(f"{k}-{v}" for k, v in freq.items())
    print("Frequency of letters:", freq_str)



