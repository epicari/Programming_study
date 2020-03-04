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
        return head
    
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
        return head
    
    def removeDuplicates(self, head):
        #print('removeDuplicates')
        current = head
        while current:
            if current.next:
                if current.data == current.next.data:
                    tmp = current.next
                    current.next = current.next.next
                    del tmp
                    continue # if문이 실행되면 continue 아래 코드는 모두 패스
            current = current.next #current.next가 존재하지 않으면 while이 멈춤
        return head

if __name__ == "__main__":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    #mylist.display(head) 
    #mylist.delete_mk2(head, 2)
    #mylist.display(head)
    mylist.removeDuplicates(head)
    mylist.display(head)