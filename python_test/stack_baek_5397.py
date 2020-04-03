#
# 백준 5397
#
#

test_case = int(input())

for _ in range(test_case):
    left = []
    right = []
    data = input()
    for i in data:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))