#
# 백준 1159
# 딕셔너리 사용

last_name = dict()
result = []

for _ in range(int(input())):
    x = input()
    if x[0] not in last_name:
        last_name[x[0]] = 1
    else:
        last_name[x[0]] += 1

for key, value in last_name.items():
    if value >= 5:
        result.append(key)

result.sort()
if result:
    print(''.join(result))
else:
    print('PREDAJA')