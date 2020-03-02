#
# HashTable
#
#
class HashTable:
    def __init__(self, length=8):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        hash_index = self.hash(key) #클래스 내 다른 함수 쓸 때 self.함수명
        
        if self.array[hash_index] is not None:
            for index in self.array[hash_index]:
                if index[0] == key:
                    index[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        else:
            self.array[hash_index] = [] # 'NoneType' object has no attribute 'append'
            self.array[hash_index].append([key, value])

    def get(self, key):
        hash_index = self.hash(key)

        if self.array[hash_index] is None:
            raise KeyError()
        else:
            for index in self.array[hash_index]:
                if index[0] == key:
                    return index[1]
            raise KeyError()

if __name__ == '__main__':
    ht = HashTable()
    ht.add('Dave', '01020300020')
    print(ht.get('Dave'))