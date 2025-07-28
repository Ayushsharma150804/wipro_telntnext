# Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
# He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.
# Hints to find the secret message:
# 1. The number of lines in the file tells you the meeting time.
# Note: 1<= number of lines <= 24
# If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
# If the number of lines is 15, then the meeting time is 3 PM.
# If the number of lines is 10, then the meeting time is 10 AM.
# 2. The word appearing for the maximum number of times tells you the meeting place.
# Note: Meeting place will be a street name.
# For example,
# If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
# If the word Park appears for the maximum number of times, then meeting place is Park Street.

def find_meeting_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)

    # Determine meeting time
    if line_count <= 12:
        meeting_time = f"{line_count} AM"
    else:
        meeting_time = f"{line_count - 12} PM"

    # Count words frequency
    word_freq = {}
    for line in lines:
        words = line.strip().split()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    # Find the word with maximum frequency
    meeting_place_word = max(word_freq, key=word_freq.get)
    meeting_place = f"{meeting_place_word} Street"

    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")


