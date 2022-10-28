# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        left2right = True
        res = []
        if root == None:
            return []

        queue = collections.deque([root])

        while queue:
            curLevelNodes = []

            num = len(queue)

            for _ in range(num):
                curNode = queue.popleft()
                curLevelNodes.append(curNode.val)

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

            if left2right:
                res.append(curLevelNodes)
            else:
                res.append(curLevelNodes[::-1])

            left2right = not left2right
            
        return res
