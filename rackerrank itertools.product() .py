# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

input_A = list(map(int, input().split()))
input_B = list(map(int, input().split()))

print(*list(product(input_A, input_B)))