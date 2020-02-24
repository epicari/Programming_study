#
#
# Doubly Linked List
#
#
#

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next

class Solution:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self, data):
        print('insert')
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head #원본 데이터가 변하지 않도록
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            self.tail = new
            new.prev = node

    def insert_before(self, data, before_data):
        print('insert before {0}'.format(before_data))
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.tail #뒤에서부터 시작
            while node.data != before_data:
                print('node data: {0}'.format(node.data))
                node = node.prev
                if node == None:    
                    print('None')
                    return
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node

    def delete(self, data):
        print('delete {0}'.format(data))
        if self.head == None:
            print('None head')
            return
        elif self.head.data == data: #현재 데이터가 삭제 될 데이터이면
            tmp = self.head #임시메모리에 넣고
            self.head = self.head.next #현재 데이터를 다음 데이터로 덮어씌우고
            del tmp #임시메모리에 넣은 현재 데이터를 삭제
            return
        else:
            node = self.head
            while node.next: #현재 데이터의 다음 데이터가 존재하면
                print('node.head: {0}'.format(node.data))
                if node.next.data == data: #그리고 다음 데이터의 데이터가 삭제 될 데이터이면
                    tmp = node.next #임시메모리에 넣고
                    node.next = node.next.next #다음 데이터를 다음 다음 데이터로 덮어씌우고
                    node.next.prev = node #다음 데이터의 이전 데이터를 현재 데이터로 바꾸고
                    node.tail = node.next #현재 데이터의 꼬리를 다음 데이터로 바꾼 뒤
                    del tmp #다음 데이터를 삭제
                    return
                else:
                    node = node.next

    def display(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next

if __name__ == '__main__':
    n = Solution(0)
    T = int(input())
    for i in range(1, T):
        n.insert(i)
    n.display()
    print()
    n.delete(2)
    n.display()
    print()
    n.insert_before(2.5, 3)
    n.display()