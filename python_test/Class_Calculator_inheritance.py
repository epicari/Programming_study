#
# class_test_calculator 상속
# 기존의 클래스 함수를 그대로 쓰거나, 추가하거나 기존 기능을 변경할 때
# 사용
#

import class_test_calculator

class MoreFourCal(class_test_calculator.FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

if __name__ == '__main__':
    n1 = MoreFourCal(5, 5)
    print(n1.add())
    print(n1.mul())
    print(n1.sub())
    print(n1.div())
    print(n1.pow())