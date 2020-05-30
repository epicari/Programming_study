#
# Hacker Rank 30 Days of Code Day 28: RegEx, Patterns, and Intro to Databases
#
#

import re

res = []

for _ in range(int(input())):
    f, e = input().split()
    if re.search('@gmail\.com$', e):
        res.append(f)

for i in sorted(res):
    print(i)