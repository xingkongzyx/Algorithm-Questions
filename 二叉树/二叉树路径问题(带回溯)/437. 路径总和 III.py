""" 
两节点间的路径和 = 两节点的前缀和之差
* 递归函数的意义: 更新以当前节点作为路径的最后一个节点时满足路径和的结果数量
/ 时间复杂度: 每个节点只遍历一次, O(N).
/ 空间复杂度: 开辟了一个hashMap, O(N).

? https://leetcode.cn/problems/path-sum-iii/solutions/596361/dui-qian-zhui-he-jie-fa-de-yi-dian-jie-s-dey6/?orderBy=most_votes
"""


class Solution:
    def pathSum(self, root, targetSum):
        if root == None:
            return 0
        preSumMap = {0: 1}
        count = 0
        currentSum = root.val
        # targetSum

        def traverse(node):
            nonlocal currentSum, preSumMap, count
            # * 这里使用前缀和从而判断是否有路径和满足 targetSum 的条件
            if currentSum - targetSum in preSumMap:
                # print(node.val, preSumMap)
                count += preSumMap[currentSum - targetSum]
            preSumMap[currentSum] = preSumMap.get(currentSum, 0) + 1
            #* 递归的终止条件, 一旦遇到了叶子节点就不会再往下继续遍历, 因为代码中没有处理空节点的逻辑
            if node.left == None and node.right == None:
                return

            #! 非常关键, 当我们遍历另一条路径时不希望已经遍历过的节点还储存在 preSumMap map 中, 这样会导致结果错误. 所以在前面遍历完左/右子树后能够将在遍历左右子树过程中加入 preSumMap map 的项撤回.
            if node.left:
                currentSum += node.left.val
                traverse(node.left)
                preSumMap[currentSum] -= 1
                currentSum -= node.left.val

            if node.right:
                currentSum += node.right.val  
                traverse(node.right)
                preSumMap[currentSum] -= 1
                currentSum -= node.right.val
            # preSum[currentSum] -= 1

        traverse(root)
        return count
