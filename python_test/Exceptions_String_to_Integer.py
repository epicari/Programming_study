#
# HackerRank Tutorials Day 16: Exceptions - String to Integer
#
# try except를 사용하기
# except [발생 오류[as 오류 메시지 변수]]:
# 또는 except: 사용 ~ 오류 종류에 상관없이 오류가 발생하면 except 사용

import sys
S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")