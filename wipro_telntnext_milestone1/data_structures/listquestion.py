# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
int_list = [10, 20, 30, 40, 50]
print("Full list:", int_list)
print("First element:", int_list[0])
print("Second element:", int_list[1])
print("Third element:", int_list[2])
print("Fourth element:", int_list[3])
print("Fifth element:", int_list[4])

# 2. Write a program to append a new item to the end of the list.
int_list.append(60)
print("List after appending 60:", int_list)

# 3. Write a program to reverse the order of the items in the list.
int_list.reverse()
print("Reversed list:", int_list)

# 4. Write a program to print the number of occurrences of a specified element in a list.
count_list = [1, 2, 3, 2, 4, 2, 5]
print("List for counting:", count_list)
element = 2
print(f"Number of occurrences of {element}:", count_list.count(element))

# 5. Write a program to append the items of list1 to list2 in the front.
list1 = [7, 8, 9]
list2 = [1, 2, 3]
list2 = list1 + list2
print("List after appending list1 to front of list2:", list2)

# 6. Write a program to insert a new item before the second element in an existing list.
sample_list = [100, 200, 300, 400]
sample_list.insert(1, 150)  # Inserting at index 1
print("List after inserting 150 before second element:", sample_list)

# 7. Write a program to remove the item from a specified index in a list.
remove_list = [5, 10, 15, 20, 25]
index_to_remove = 2
removed_item = remove_list.pop(index_to_remove)
print(f"List after removing item at index {index_to_remove} ({removed_item}):", remove_list)

# 8. Write a program to remove the first occurrence of a specified element from a list.
first_occurrence_list = [11, 22, 33, 22, 44]
element_to_remove = 22
first_occurrence_list.remove(element_to_remove)
print(f"List after removing first occurrence of {element_to_remove}:", first_occurrence_list)
