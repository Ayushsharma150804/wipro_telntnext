# 1. Write a program to read the entire content from a txt file and display it to the user.
filename = input("Enter file name: ")
with open(filename, 'r') as file:
    content = file.read()
print(content)


# 2. Write a program to read first n lines from a txt file. Get n as user input.
n = int(input("Enter number of lines to read: "))
with open(filename, 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')


# 3. Write a program to accept input from user and append it to a txt file.
append_text = input("Enter text to append: ")
with open(filename, 'a') as file:
    file.write(append_text + '\n')


# 4. Write a program to read contents from a txt file line by line and store each line into a list.
lines_list = []
with open(filename, 'r') as file:
    for line in file:
        lines_list.append(line.rstrip('\n'))
print(lines_list)


# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
with open(filename, 'r') as file:
    text = file.read()
words = text.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)


# 6. Write a program to count the frequency of a user entered word in a txt file.
search_word = input("Enter word to count frequency: ")
with open(filename, 'r') as file:
    text = file.read()
words = text.split()
count = words.count(search_word)
print(f"Frequency of '{search_word}':", count)
