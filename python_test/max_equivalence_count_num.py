def solution(A):
    c = [0] * 100000

    for i in range(len(A)):
        c[A[i]] += 1
    
    for j in range(len(A)):
        if A[j] == max(c):
            return max(c)
    
    return 0

A = [3, 8, 2, 3, 3, 2]
B = [7, 1, 2, 8, 2]
C = [3, 1, 4, 1, 5]
D = [5, 5, 5, 5, 5]

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))