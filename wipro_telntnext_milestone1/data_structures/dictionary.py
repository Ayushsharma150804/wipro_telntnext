# 1. Write a program to add a key and value to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated dictionary:", sample_dict)

# 2. Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionaries: dic1={1:10, 2:20}, dic2={3:30, 4:40}, dic3={5:50, 6:60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined_dict = {}
for d in (dic1, dic2, dic3):
    combined_dict.update(d)
print("Concatenated dictionary:", combined_dict)

# 3. Write a program to check if a given key already exists in a dictionary.
check_dict = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
if key in check_dict:
    print(f"Key '{key}' exists in the dictionary.")
else:
    print(f"Key '{key}' does not exist in the dictionary.")

# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
iterate_dict = {'x': 1, 'y': 2, 'z': 3}
print("Keys:")
for key in iterate_dict:
    print(key)
print("Values:")
for value in iterate_dict.values():
    print(value)
print("Keys and Values:")
for key, value in iterate_dict.items():
    print(f"{key}: {value}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of the keys.
square_dict = {}
for i in range(1, 16):
    square_dict[i] = i ** 2
print("Dictionary of squares from 1 to 15:", square_dict)

# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
sum_dict = {'a': 100, 'b': 200, 'c': 300}
total = sum(sum_dict.values())
print("Sum of all values in the dictionary:", total)