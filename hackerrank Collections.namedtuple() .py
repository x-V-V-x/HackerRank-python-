""" Collections.namedtuple() 
Task
Dr. John Wesley has a spreadsheet containing a list of student’s IDs, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

Average = Sum of all marks / Total Students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won’t change.) """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))