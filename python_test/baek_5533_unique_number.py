#
# 백준 5533 유니크
#
#

n = int(input())
players = []
scores = [0] * n

for _ in range(n):
    players.append(list(map(int, input().split())))

for i in zip(*players): #zip(*iterable), 같은 길이로 이루어진 자료형 묶어줌
    for j, score in enumerate(i): #enumerate 인덱스와 값 리턴
        if i.count(score) == 1:
            scores[j] += score

for score in scores:
    print(score)