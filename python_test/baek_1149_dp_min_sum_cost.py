#
# 백준 1149 
# DP 
#

def solution(arr): 
    for i in range(1, len(arr)):
        # R
        arr[i][0] = arr[i][0] + min(arr[i-1][1], arr[i-1][2])
        # G
        arr[i][1] = arr[i][1] + min(arr[i-1][0], arr[i-1][2])
        # B
        arr[i][2] = arr[i][2] + min(arr[i-1][1], arr[i-1][0])
        
    return min(arr[len(arr)-1][0], arr[len(arr)-1][1], arr[len(arr)-1][2])

if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(int(input()))]
    print(solution(arr))