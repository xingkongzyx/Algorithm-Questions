# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        self.preSum = {0: 1}
        self.count = 0
        self.currentSum = root.val
        self.target = targetSum

        def traverse(node):
            found = self.currentSum - self.target
            if found in self.preSum:
                print(node.val, self.preSum)
                self.count += self.preSum[found]

            if self.currentSum in self.preSum:
                self.preSum[self.currentSum] += 1
            else:
                self.preSum[self.currentSum] = 1
            # self.preSum[self.currentSum] = self.preSum.get(self.currentSum, 0) + 1

            if node.left == None and node.right == None:
                return 

            if node.left:
                self.currentSum += node.left.val
                traverse(node.left)
                self.preSum[self.currentSum] -= 1
                self.currentSum -= node.left.val

            if node.right:
                self.currentSum += node.right.val
                traverse(node.right)
                self.preSum[self.currentSum] -= 1
                self.currentSum -= node.right.val
            # self.preSum[self.currentSum] -= 1

        traverse(root)
        return self.count
