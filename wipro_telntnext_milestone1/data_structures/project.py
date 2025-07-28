# Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

# Sample output:

# Jeff: is afraid of Dogs.

# David: Plays the piano.

# Jason: Can fly an airplane.

# Jeff: is afraid of heights.

# David: Plays the piano.

# Jason: Can fly an airplane.

# Jill: Can hula dance.
# Initial dictionary of people and their interesting facts
people_facts = {
    "Jeff": "is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display the original dictionary
print("Original list of people and facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# Modify Jeff's fact
people_facts["Jeff"] = "is afraid of heights."

# Add a new person and their fact
people_facts["Jill"] = "Can hula dance."

# Display the updated dictionary
print("\nUpdated list of people and facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


# Given the participant's score sheet for your University Sports Day,
#  you are required to find the runner-up score. You have scores.
#  Store them in a list and find the score of the runner-up.

scores = [2, 3, 6, 6, 5]
unique_scores = sorted(set(scores), reverse=True)
runner_up = unique_scores[1]
print("Runner-up score:", runner_up)

# You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.
# 
# Student's name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.
# 
# Formula: (sum of marks) / (no of subjects)
# 
# Sample input: ("Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60])
# 
# Sample output:
# Enter a name: Malika
# Average percentage mark: 56
# 
# Explanation:
# Marks for Malika are [52, 56, 60] whose average is (52+56+60)/3 = 56

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")
if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", round(average))
else:
    print("Student not found.")

# Given a string of n words, help Alex to find out how many times his name appears in the string.
# 
# Constraint: 1 <= n <= 200
# 
# Sample input: Hi Alex WelcomeAlex Bye Alex.
# 
# Sample output: 3
# 
# Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.

text = "Hi Alex WelcomeAlex Bye Alex."
count = text.count("Alex")
print(count)
