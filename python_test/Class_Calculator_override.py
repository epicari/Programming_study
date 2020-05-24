#
# Class_Calculator_base 오버라이딩
# 기존의 클래스 함수 내용을 재정의 할 때 사용
# 
#

import Class_Calculator_base as base

class MoreFourCal(base.FourCal):
    def div(self):
        if self.first == 0 or self.second == 0: return 0
        else: 
            return self.first / self.second

if __name__ == '__main__':
    n1 = MoreFourCal(5, 0)
    print(n1.add())
    print(n1.mul())
    print(n1.sub())
    print(n1.div())
