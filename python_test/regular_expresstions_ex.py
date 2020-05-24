#
# 정규표현식 공부
# 참고: https://wikidocs.net/1642
#

import re

#S = "13 DUP 4 POP 5 DUP + DUP + -"

#print(re.findall(r""))

p = re.compile('[a-z]+')
print(p)
m1 = p.match('python')
print(m1)
m2 = p.match('3 python') #3은 문자열이 아니므로 None
print(m2)
s1 = p.search('python')
print(s1)
s2 = p.search('3 python') #3 이후 python이 매칭됨
print(s2)
print(s2.group())
print(s2.start())
print(s2.end())
print(s2.span())
fa = p.findall('life is to short')
print(fa)