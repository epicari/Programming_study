#
# HackerRank Tutorials Day 11: 2D Arrays
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#


if __name__ == '__main__' :
    arr = []
    sum = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    
    print(max(sum))