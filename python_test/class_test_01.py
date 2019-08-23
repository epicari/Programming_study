class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b

a = Cal(3, 4)
print(a.add())
print(a.mul())

b = Cal(5, 5)
print(b.add())
print(b.mul())