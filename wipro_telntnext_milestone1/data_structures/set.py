# 1. Write a program to remove a given item from the set.
sample_set = {10, 20, 30, 40, 50}
item_to_remove = 30
sample_set.discard(item_to_remove)  # discard() won't raise an error if item is not found
print("Set after removing item:", sample_set)

# 2. Write a program to create an intersection of sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# 3. Write a program to create a union of sets.
union_set = set1.union(set2)
print("Union of sets:", union_set)

# 4. Write a program to find the maximum and minimum value in a set.
number_set = {15, 2, 89, 43, 6}
max_value = max(number_set)
min_value = min(number_set)
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)
