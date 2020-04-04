#
# lambda 인자 : 표현식
#
#

def add(x, y):
    return x + y

if __name__ == "__main__":
    x, y = map(int, input().split(' '))
    print(add(x, y))

    print((lambda a, b: a + b)(x, y))

    print(list(map(lambda x: x ** 2, range(y))))

