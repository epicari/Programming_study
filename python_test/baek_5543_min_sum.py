#
# 백준 5534
#
#
arr = []
for _ in range(5):
    price = int(input())
    if price >= 100 and price <= 2000: 
        arr.append(price)
    else:
        print("가격 범위 초과")

print(min(arr[:3])+min(arr[3:])-50)