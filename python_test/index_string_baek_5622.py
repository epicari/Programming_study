#
# 백준 5622
# 2중 반복문을 사용 한 부분과 index를 사용한 카운팅
#

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0
s = input()

for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            count += dial.index(j) + 3

print(count)