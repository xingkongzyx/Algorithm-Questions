# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        if root == None:
            return 0
        self.preSumMap = {0: 1}
        self.count = 0
        self.currentSum = root.val
        # targetSum

        def traverse(node):
            #* 这里使用前缀和从而判断是否有路径和满足 targetSum 的条件
            if self.currentSum - targetSum in self.preSumMap:
                # print(node.val, self.preSumMap)
                self.count += self.preSumMap[self.currentSum - targetSum]

            if self.currentSum in self.preSumMap:
                self.preSumMap[self.currentSum] += 1
            else:
                self.preSumMap[self.currentSum] = 1

            #* 递归的终止条件, 一旦遇到了叶子节点就不会再往下继续遍历, 因为代码中没有处理空节点的逻辑
            if node.left == None and node.right == None:
                return 
            #! 非常关键, 当我们遍历另一条路径时不希望已经遍历过的节点还储存在 preSumMap map 中, 这样会导致结果错误. 所以在前面遍历完左/右子树后能够将在遍历左右子树过程中加入 preSumMap map 的项撤回.
            if node.left:
                self.currentSum += node.left.val
                traverse(node.left)
                #* 这里撤回的其实是在 遍历到 node.left 时加入到 map 中的 [ self.currentSum + node.left.val] 的项
                self.preSumMap[self.currentSum] -= 1
                self.currentSum -= node.left.val

            if node.right:
                self.currentSum += node.right.val
                traverse(node.right)
                self.preSumMap[self.currentSum] -= 1
                self.currentSum -= node.right.val
            # self.preSum[self.currentSum] -= 1

        traverse(root)
        return self.count
