class Animal():
    def __init__(self, name, age): #생성자, 객체에 초기값을 설정해야 할 때 사용
        self.name = name
        self.age = age
        
    def setName(self):
        return 'Animal name is '+ self.name
    
    def setAge(self):
        return 'Animal age is ' + self.age

if __name__ == "__main__": #외부에서 이 클래스를 사용할 땐 실행되지 못하게 방지

    animal = Animal('boby', '5')
    print(animal.setName())
    print(animal.setAge())

    cat = Animal('naby', '2')
    print(cat.setName())
    print(cat.setAge())