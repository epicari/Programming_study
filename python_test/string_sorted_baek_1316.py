#
# 백준 1316
# list(s)를 하면 문자열이 각각 리스트에 들어감
# sorted(s, key=s.find)를 사용하면 s에서 찾아지는 캐릭터 순으로 정렬
# s = happy 일 때,
# list(s) = ['h', 'a', 'p', 'p', 'y']
# sorted(s, key=s.find) = ['h', 'a', 'p', 'p', 'y']

count = 0
for _ in range(int(input())):
    s = input()
    if list(s) == sorted(s, key=s.find): 
        count += 1
print(count)