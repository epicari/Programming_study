#
# 백준 1874
#

n = int(input())

stack = []
result = []
count = 1 #count를 초기화 하지 않으므로 입력 된 data와 비교, +를 할지 말지 정할 수 있음

for i in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

print('\n'.join(result))