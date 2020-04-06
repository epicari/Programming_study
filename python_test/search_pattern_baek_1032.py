#
# 백준 1032
# print(''.join(['A', 'B'][True])) ... True = 1이므로 'B'가 출력됨
# 

#N=int(input())
#*x,=(input()for _ in range(N)) #x = [input() for _ in range(N)]
#print(''.join([i[0],'?'][i.count(i[0])<N] for i in zip(*x)))

test_case = int(input())
file_names = [input() for _ in range(test_case)]
pattern = list(file_names[0]) #리스트로 안 만들 시 특정 인덱스에 새로운 값 할당이 안 됨
for name in file_names[1:]:
    for i in range(len(name)):
        if name[i] != pattern[i]:
            pattern[i] = '?'

print(''.join(pattern))