# Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-).
# You like all the numbers in string 1 and dislike all the numbers in string 2.
# Third string contains the numbers given to you. Your initial happiness is 0.
# When you encounter a number which is present in string 1, add 1 to your happiness,
# if it is present in string 2, add -1 to your happiness.
# Otherwise, your happiness does not change. Output your final happiness at the end.

import sys

str1 = sys.argv[1]
str2 = sys.argv[2]
str3 = sys.argv[3]

like_set = set(str1.split('-'))
dislike_set = set(str2.split('-'))
given_nums = str3.split('-')

happiness = 0
for num in given_nums:
    if num in like_set:
        happiness += 1
    elif num in dislike_set:
        happiness -= 1

print(happiness)
