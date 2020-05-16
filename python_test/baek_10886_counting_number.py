#
# 백준 10886
#
m = []
for i in range(int(input())):
    m.append(int(input()))
if m.count(0) > m.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')