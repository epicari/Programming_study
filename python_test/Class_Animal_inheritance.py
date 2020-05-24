import Class_Animal_base as base

class inher(base.Animal): #상속, 기존 클래스 기능 확장... 기존 것 수정 못 할때
    def prof(self):
        return self.name + ' is ' + self.age

a = inher('naan', '5')
print(a.prof())
