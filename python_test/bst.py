#
# binary serach tree
#

import random

def binary_search(data, num):
    print(data)

    if len(data) == 1 and num == data[0]:
        return True
    
    if len(data) == 1 and num != data[0]:
        return False
    
    if len(data) == 0:
        return False

    m = len(data) // 2
    
    if num == data[m]:
        return True
    else:
        if num > data[m]:
            return binary_search(data[m+1:], num)
        else:
            return binary_search(data[:m], num)

if __name__ == "__main__":
    num = random.sample(range(100), 10)
    num.sort()
    binary_search(num, 52)
    