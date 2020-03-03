#
# HackerRank Tutorial Day 22: Binary Search Trees
# 삽입 및 높이만 확인, 탐색 및 삭제는 따로 넣어야 함
#
# 테스트 케이스 7 3 5 2 1 4 6 7
# 테스트 케이스 결과 3
#
#

from collections import deque
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
        if root:
            leftDepth = self.getHeight(root.left) # 계속 내려가면서 값 확인, 실행 된 함수는 스택에 쌓이면서 리턴 기다림
            rightDepth = self.getHeight(root.right)
            return max(leftDepth, rightDepth) + 1
        else:
            return -1

    def levelOrder(self, root):
        #Write your code here
        if root:
            q = deque([root])
        # 부모를 queue에 넣고 출력, 이후 부모의 자식들이 존재할 때마다 queue에 삽입, 자식의 자식이 존재하면 queue에 삽입 ...
        while q:
            n = q.popleft()
            print(n.data, end=' ')

            if n.left: q.append(n.left)
            if n.right: q.append(n.right)

if __name__ == '__main__':
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)       
    myTree.levelOrder(root)