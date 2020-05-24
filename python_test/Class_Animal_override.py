import Class_Animal_base as base

class override(base.Animal): #오버라이딩, 기존 클래스 기능 수정
    def setName(self):
        return self.name + ' is my animal name'
    
b = override('naan', '5')
print(b.setName())
