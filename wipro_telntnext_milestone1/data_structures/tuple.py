# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
sample_tuple = (5, 10, 15, 20, 25, 30, 35, 40)
print("4th element from start:", sample_tuple[3])
print("4th element from end:", sample_tuple[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
element_tuple = (1, 3, 5, 7, 9)
element = 5
if element in element_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Write a program to convert a list into a tuple.
sample_list = [100, 200, 300, 400]
converted_tuple = tuple(sample_list)
print("Converted tuple:", converted_tuple)

# 4. Write a program to find the index of an item in a tuple.
index_tuple = ('a', 'b', 'c', 'd', 'e')
item = 'c'
index = index_tuple.index(item)
print(f"Index of '{item}':", index)

# 5. Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_list = [t[:-1] + (100,) for t in tuple_list]
print("Modified list:", modified_list)
