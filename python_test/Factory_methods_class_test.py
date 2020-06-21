#
# 팩토리 메소드 테스트
#
#

from abc import ABCMeta, abstractmethod

class Robot(metaclass=ABCMeta):
    @abstractmethod #추상메소드 선언
    def getname(self): pass

class SuperRobot(Robot):
    def getname(self):
        return'SuperRobot'

class PowerRobot(Robot):
    def getname(self):
        return'PowerRobot'

class RobotFactory: #인스턴스 클래스 선언
    def getRobot(self, name):
        return name.getname()

if __name__ == "__main__":
    a = RobotFactory()
    print(a.getRobot(SuperRobot()))
    print(a.getRobot(PowerRobot()))