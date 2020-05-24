# 
# 정규표현식 re
# try-except, 에러 종류 모르면 Exception 사용
# try: except Exception as ex: print(ex) 에러종류 프린트함
#

import re

def solution(S):
    data = re.split(' ', S)
    stack = []

    for i in data:
        try:
            if i == 'DUP':
                stack.append(stack[-1])
            elif i == 'POP':
                stack.pop()
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(stack.pop() - stack.pop())
            else:
                stack.append(int(i))
        except Exception:
            return -1
    
    return stack.pop()

S = ['13 DUP 4 POP 5 DUP + DUP + -', '5 6 + -', '3 DUP 5 - -']

for i in S:
    print(solution(i))