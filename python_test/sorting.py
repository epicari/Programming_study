#
#
# Sorting
#
# 분할정복 시간복잡도 O(n log n) , 두개로 쪼개 n번 비교하므로 ,, 
# 퀵소트의 경우 평균 O(n log n), 최악은 O(n^2) 피봇이 가장 작으면 피봇을 제외한 노드끼리 비교하므로
# 퀵소트는 배열 하나만 사용하므로 공간복잡도는 O(n)
# 그 외 병합정렬, 힙정렬은 O(n log n), 
# 공간복잡도는, 병합정렬은 비교를 위해 2개의 배열을 생성하므로 O(1), 힙정렬은 데이터 요소만큼 사용하므로 O(n)
# 선택정렬은 전체 비교하므로 O(n^2), 공간복잡도는 배열 하나만 사용하므로 O(n)
# 버블정렬, 삽입정렬은 전체비교로 O(n^2), 최상은 한번 비교해 O(n), 공간복잡도는 O(n)
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

    def quick(self, d): # pivot 기준으로 정렬하여 쪼갠 뒤 병합
        if len(d) <= 1:
            return d

        pivot = d[0]

        left = [item for item in d[1:] if pivot > item]
        right = [item for item in d[1:] if pivot <= item]

        return self.quick(left) + [pivot] + self.quick(right)

    def merge(self, d): #분할 후 정렬, 마지막에 병합
        if len(d) <= 1:
            return d

        m = int(len(d) // 2)
        left = self.merge(d[:m])
        right = self.merge(d[m:])

        return self.merge_mgt(left, right)

    def merge_mgt(self, left, right):
        merged = []
        leftCount, rightCount = 0, 0

        while len(left) > leftCount and len(right) > rightCount:
            if left[leftCount] > right[rightCount]:
                merged.append(right[rightCount])
                rightCount += 1
            else:
                merged.append(left[leftCount])
                leftCount += 1
        
        while len(left) > leftCount:
            merged.append(left[leftCount])
            leftCount += 1
        
        while len(right) > rightCount:
            merged.append(right[rightCount])
            rightCount += 1
        
        return merged

if __name__ == '__main__':
    data = random.sample(range(100), 10)
    print("RawData: ", data)
    s = Sort(data)
    print("bubble:  ", s.bubble())
    print("select:  ", s.select())
    print("insert:  ", s.insert())
    print("quick:   ", s.quick(data))
    print("merge:   ", s.merge(data))