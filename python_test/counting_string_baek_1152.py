#
# 백준 1152
#
#

x = list(input().split(' '))    

#while '' in x:
#    x.remove('')

x = [i for i in x if i != '']
print(len(x))