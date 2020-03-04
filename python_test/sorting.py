#
#
# Sorting
#
#
import random

class Sort:
    def __init__(self, data):
        self.data = data

    def select(self): # 최솟값을 찾고 맨 앞으로 이동, 이후 교환한 자리를 제외하여 반복
        for stand in range(len(data) - 1):
            lowest = stand
            for index in range(stand + 1, len(data)):
                if data[lowest] > data[index]:
                    lowest = index
            data[lowest], data[stand] = data[stand], data[lowest]
        return self.data

    def bubble(self): # 앞에서부터 차례대로 비교 후, 뒷값보다 크면 교환 후 계속 진행
        for index in range(len(data) - 1):
            swap = False
            for index2 in range(len(data) - index - 1):
                if data[index2] > data[index2 + 1]:
                    data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                    swap = True
            if swap is False:
                break
        return self.data

    def insert(self): # 두번째 값을 기준으로, 앞의 값부터 맨 앞까지 비교 후 작으면 교환
        for index in range(len(data) - 1):
            for index2 in range(index + 1, 0, -1):
                if data[index2] < data[index2 - 1]:
                    data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
                else:
                    break
        return self.data

    def quick(self):
        pass

    def marge(self):
        pass

if __name__ == '__main__':
    data = random.sample(range(100), 10)
    print(data)
    s = Sort(data)
    print(s.bubble())
    print(s.select())
    print(s.insert())
    

