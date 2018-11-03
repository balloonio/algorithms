# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

size = 0
array = []

for i, line in enumerate(sys.stdin):
    if i == 0:
        size = int(line.strip("\n"))
    else:
        array = [word for word in line.split(" ")]

"""
stdin:
3
hello world bolooooon
"""
print(size)
print(array)
"""
stdout:
Output:
3
['hello', 'world', 'bolooooon']
"""
