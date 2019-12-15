#
# HackerRank Tutorials Day 15: Linked List
#
# 리스트에 삽입할 때, head에 넣을지 아니면 head 다음에 넣을지 판단해야 함
#

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

if __name__ == "__main__":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head) 