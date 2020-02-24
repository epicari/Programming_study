#
# HackerRank Tutorial Day 22: Binary Search Trees
# 삽입 및 높이만 확인, 탐색 및 삭제는 따로 넣어야 함
#
# 테스트 케이스 7 3 5 2 1 4 6 7
# 테스트 케이스 결과 3
#
#

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data) #root=data 등록
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        return 

if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)       