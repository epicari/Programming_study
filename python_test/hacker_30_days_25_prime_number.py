#
# Hacker Rank 30 Days of Code Day 25: Running Time and Complexity
#

from math import sqrt

def prime_num(num):
    if x < 2: return "Not prime"
    elif x == 2: return "Prime"

    sq = int(sqrt(num))
    for i in range(2, sq+1):
        if num % i == 0:
            return "Not prime"
    return "Prime"

for _ in range(int(input())):
    x = int(input())
    print(prime_num(x))