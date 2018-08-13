""" 
Description
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Given a parameter m, and find the last day of m group flowering at the same time(each group has at least k plots)

If there isn't such day, output -1.

Example
input:
flowerded = [1,3,2]
k = 1
m = 2
output:
2
"""
