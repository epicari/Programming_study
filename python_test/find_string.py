#
# Find String
# 
# 리스트 내포(list comprehension) 사용하면 편 함
# [표현식 for 항목 in 반복가능객체 if 조건문]
# 

a = 'ABCDCDC'
b = 'CDC'
count = 0

print(len([i for i in range(len(a)) if a[i:i+len(b)] == b]))

for i in range(len(a)):
    if a[i:i+len(b)] == b:
        count += 1
print(count) 