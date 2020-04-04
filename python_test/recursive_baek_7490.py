#
# 백준 7490
# 재귀
#

import copy

def recursive(arr, n):
    if len(arr) == n:
        operators.append(copy.deepcopy(arr))
        return
        
    arr.append(' ')
    recursive(arr, n)
    arr.pop()

    arr.append('+')
    recursive(arr, n)
    arr.pop()

    arr.append('-')
    recursive(arr, n)
    arr.pop()

test_case = int(input())

for _ in range(test_case):
    operators = []
    n = int(input())
    recursive([], n - 1)

    integers = [i for i in range(1, n + 1)]

    for ope in operators:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + ope[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()