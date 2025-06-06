""" Collections.deque() 
Task
Perform append, pop, popleft and appendleft methods on an empty deque d. """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

D = deque()

for _ in range(int(input())):
    oper, val, *args = input().split() + ['']
    eval(f'D.{oper} ({val})')
print(*D)