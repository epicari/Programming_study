#
# HackerRank Tutorials Day 15: Linked List
#
# 리스트에 삽입할 때, head에 넣을지 아니면 head 다음에 넣을지 판단해야 함
#
# 02.24.2020, insert_mk2, delete 추가

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method    
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head

    def insert_mk2(self, head, data):
        if head == None:
            head = Node(data)
        else:
            node = head
            while node.next:
                node = node.next
            node.next = Node(data)
        return node
    
    def delete_mk2(self, head, data):
        if head == None:
            print('None')
            return
        elif head.data == data:
            tmp = head
            head = head.next
            del tmp
        else:
            node = head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                    return
                else:
                    node = node.next

if __name__ == "__main__":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head) 
    mylist.delete_mk2(head, 2)
    mylist.display(head)