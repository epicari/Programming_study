#
# 백준 1966
#
#

# priority_num이 가장 큰 순으로 queue에서 빼야 함
# priority_num을 회전시키면서 동시에 count += 1을 하다가
# max(priority_num) == queue[location_num]이 되면 count 반환 후 종료
#

test_case = int(input())

for _ in range(test_case):
    num, location_num = map(int, input().split())
    priority_num = list(map(int, input().split()))
    priority_num = [(i, idx) for idx, i in enumerate(priority_num)]
    count = 0

    while True:
        if priority_num[0][0] == max(priority_num, key=lambda x: x[0])[0]:
            count += 1
            if priority_num[0][1] == location_num:
                print(count)
                break
            else:
                priority_num.pop(0)
        else:
            priority_num.append(priority_num.pop(0))