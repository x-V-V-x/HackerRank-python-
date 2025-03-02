"""hackerrank Array Mathematics
Task

You are given two integer arrays, A and B of dimensions N X M.
Your task is to perform the following operations:

Add (A + B)
Subtract (A – B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array .
The following N lines contains M space separated integers of array B.


Output Format
Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
"""

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')