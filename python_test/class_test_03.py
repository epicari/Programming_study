import class_test_01

class reNaming(class_test_01.Animal): #오버라이딩, 기존 클래스 기능 수정
    def setName(self):
        return self.name + ' is my animal name'
    
b = reNaming('naan', '5')
print(b.setName())
