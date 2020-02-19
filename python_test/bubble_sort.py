#!/bin/python3

import sys

n = int(input().strip()) #3
a = list(map(int, input().strip().split(' '))) #1 2 3
# Write Your Code Here
numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
    
print('Array is sorted in {0} swaps.'.format(numberOfSwaps))
#print('First Element: {0}'.format(a[0]))
#print('Last Element: {0}'.format(a[-1]))
print(a)