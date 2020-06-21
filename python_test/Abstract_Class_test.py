#
# 추상 클래스 테스트
#
#

from abc import ABCMeta, abstractmethod

class AbstactCountry(metaclass=ABCMeta): #추상클래스
    name = '국가명'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드')

    @abstractmethod
    def show_capital(self): pass

class Country(AbstactCountry): #추상클래스 상속
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def show_name(self):
        print('국가 이름: ', self.name)
    
    def show_capital(self):
        #super().show_capital() #추상메소드 사용 시 넣어야 함
        print('수도: ', self.capital)

if __name__ == "__main__":
    #a = AbstactCountry() #추상메소드 추가 후 객체 생성 시 오류 남
    b = Country('대한민국', '서울')
    b.show_name()
    b.show_capital()