#Write a program to find check if a string has only octal digits. Given string ['789', '123', '004']

import re

strings = ['789', '123', '004']

pattern = r'^[0-7]+$'

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' contains only octal digits.")
    else:
        print(f"'{s}' does NOT contain only octal digits.")

#Extract the user id, domain name and suffix from the following email addresses. emails """zuck@facebook.com
#sunder33@google.com
#jeff42@amazon.com"""

import re
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'

matches = re.findall(pattern, emails)

for user, domain, suffix in matches:
    print(f"User ID: {user}, Domain: {domain}, Suffix: {suffix}")

#Split the following irregular sentence into proper words
# sentence"""A, very very; irregular_sentence""" ## expected outout: A very very irregular
# Regular Expression

import re

sentence = "A, very very; irregular_sentence"
words = re.split(r'\W+', sentence)
cleaned_sentence = ' '.join(filter(None, words))
print(cleaned_sentence)

#Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt ørstats"""

import re

tweet = """Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt ørstats"""

tweet = re.sub(r'RT|cc|CC', '', tweet)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'[^\w\s]', '', tweet)
tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)

#Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# Code to retrieve the HTML page is given below:
# import requests
# r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
# r.text # html text is contained here
import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

text_contents = re.findall(r'>([^<]+)<', html)

cleaned_texts = [text.strip() for text in text_contents if text.strip()]

for text in cleaned_texts:
    print(text)

#Given below list of words, identify the words that begin and end with the same character.
# civic
# trust
# widows
# maximum
# museums
# aa
# as

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

matching_words = [word for word in words if word[0] == word[-1]]

print("Words that begin and end with the same character:")
print(matching_words)
