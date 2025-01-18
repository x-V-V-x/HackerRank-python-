""" Compress the String!
Task
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools .


You are given a string S. Suppose a character ‘c‘ occurs consecutively X times in the string. Replace these consecutive occurrences of the character ‘c‘ with (X, c) in the string  """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')