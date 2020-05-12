#
# 백준 2577
#
#

# 풀이법 1
def my_counting(i):
    arr = [0] * 10

    for k in list(str(i)):
        arr[int(k)] += 1

    for n in arr:
        print(n)

# 풀이법 2
def my_counting_mk2(i):
    arr = list(str(i))
    for j in range(10):
        result = arr.count(str(j))
        print(result)
    
i = 1
for _ in range(3):
    j = int(input())
    i *= j

#my_counting(i)
my_counting_mk2(i)

