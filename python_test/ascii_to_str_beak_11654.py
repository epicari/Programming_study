#
# 백준 11654
#
#

s = input()

if type(s) == int:
    print(chr(s))
elif type(s) == str:
    print(ord(s))
else:
    print('None')
