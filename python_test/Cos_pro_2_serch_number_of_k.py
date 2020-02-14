#
# COS Pro 2급 Python 모의고사 k번째로 작은 수
# 2차원 배열 arr에서 k번째로 작은 수 찾기
# 나는 arr[i][j]로 생각해서 for을 두 번 돌렸으나,
# Python에선 for 1번만 써도 됨..
# 


def solution_my(arr, k):
    answer = 0
    sort_list = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            sort_list.append(arr[i][j])
    sort_list.sort(reverse=True)
    
    for i in range(k-1):     
        sort_list.pop()
    answer = sort_list.pop()
    
    return answer

def solution_answer(arr, k):
    answer = 0
    sort_list = []
    
    for i in arr:
        sort_list += i
    
    sort_list.sort()
    answer = sort_list[k-1]
    return answer

arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k = 4

solution_answer(arr, k)
