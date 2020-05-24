#
# __init__를 사용하면 생성자가 됨, 따라서 n1 = FourCal(4, 2) 처럼
# n1 = setdata(4, 2)를 따로 안 거쳐도 됨.
# 

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        print('생성자')

    def setdata(self, first, second):
        self.first = first
        self.second = second
        print('setdata')

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

if __name__ == '__main__':
    n1 = FourCal(4, 2)
    #n1.setdata(4, 2)
    print(n1.add())
    print(n1.mul())
    print(n1.sub())
    print(n1.div())

