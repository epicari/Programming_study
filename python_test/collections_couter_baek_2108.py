#
# 백준 2108
#
#
# 산술평균: N개의 수들의 합을 N으로 나눈 값
# 중앙값: N개의 수들을 증가하는 순서로 나열, 그 중앙에 위치하는 값
# 최빈값: N개의 수들 중 가장 많이 나타나는 값, 여러 개가 있을 경우 두 번째로 작은 값
# 범위: N개의 수들 중 최댓값과 최솟값의 차이
import sys
from collections import Counter

def counting(m):
    m_dict = Counter(m) # 각 num에 대해 빈도수를 dict로 만들어 줌
    ms = m_dict.most_common() # Couting 한 수를 튜플 형태로 반환
    #print("Couting한 결과: ", ms)
    if len(m) > 1:
        if ms[0][1] == ms[1][1]:
            return ms[1][0]
        else:
            return ms[0][0]
    else:
        return ms[0][0]

N = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for _ in range(N)]

print(round(sum(m) // N, 1))
m.sort()
print(m[int(len(m)) // 2])
print(counting(m))
print(max(m) - min(m)) #사전에 정렬 했으므로 m[-1] - m[0]로 바꿀 수 있음