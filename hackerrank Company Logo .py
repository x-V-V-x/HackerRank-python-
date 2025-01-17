"""Company Logo
Task
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,


GOOGLE would have it’s logo with the letters G, O, E. """

# importing the modules
import math
import os
import random
import re
import sys
from collections import Counter


# using __name__ variable
if __name__ == '__main__':
    
    # taking input from user and sorting it
    s = input()
    s = sorted(s)
    
    # using counter method to find the frequency of each of the words
    FREQUENCY = Counter(list(s))
    
    # using for loop to print the three words with frequency
    for k, v in FREQUENCY.most_common(3):
        print(k, v)