class Test:
    def __init__(self, num):
        self.num = num

    def add_list(self):
        self.num[0], self.num[1] = self.num[1], self.num[0]
        return self.num
            
arr = [10, 5]
arr_ = Test(arr)
print(arr_.add_list())
