#
# Binary Tree
#

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        print("insert")
        self.current_node = self.root

        while True:
            if value < self.current_node.value: #Return is True, Left
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    
    def search(self, value):
        print("search")
        self.current_node = self.root

        while self.current_node:
            if value == self.current_node.value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        
        return False

    def delete(self, value):
        print("delete")
        
        searched = False
        self.current_node = self.root
        self.parent_node = self.root

        #삭제 할 노드가 존재하는지 탐색
        while self.current_node: 
            if value is self.current_node:
                searched == True
                break
            elif value < self.current_node.value:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right

        if searched is False:
            return False

        # 리프 노드인지 확인
        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent_node.value:
                self.parent_node.left = None
            else:
                self.parent_node.right = None
        
        # 아이 노드를 하나 가지고 있을 경우 (left, right 각각 케이스로 나눠야 함)
        elif self.current_node.left is not None and self.current_node.right is None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left
        
        elif self.current_node.left is None and self.current_node.right is not None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right
        
        # 아이 노드를 두개 가지고 있을 경우 (left, right 각각 케이스로 나눠야 함)
        elif self.current_node.left is not None and self.current_node.right is not None:
            if value < self.parent_node.value: #left
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent_node.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                
            else: #right
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        
        return True

if __name__ == "__main__":
    num = set()
    
    while len(num) is not 100:
        num.add(random.randint(0, 999))

    root = Node(500)
    bst = Solution(root)

    for n in num: #랜덤 숫자 100개를 이진 트리에 입력
        bst.insert(n)

    for n in num: #랜덤 숫자 100개를 이진 트리에서 탐색
        if bst.search(n) is False:
            print("search failed: ", n)
    
    del_num = set()
    while len(del_num) is not 10:
        del_num.add(random.randint(0, 99))

    for n in del_num: #랜덤 숫자 10개를 이진 트리에서 삭제 
        if bst.delete(n) is False:
            print("delete failed: ", n)
