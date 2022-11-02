
""" 
* 涉及到回溯，因为我们要把路径(currentPath)记录下来,需要回溯来回退一个路径,再进入另一个路径。
* 回溯和递归是一一对应的，有一个递归，就要有一个回溯. 并且它们要放在同一个括号里
/ People who are saying time complexity is O(n) are wrong IMHO. Yes it is true that you need to visit every node at least once, so that contributes O(n) to the total time complexity. But then at the same time when you reach the leaf, you need to generate the path and add it to the ans array, which will be O(logN) time in the case when tree has some leaves on both sides. And when the tree is somewhat balanced, you can take the number of leaves as half of the number of nodes in the tree, as an upper bound. So, that gives you O(n/2 + (n/2)logn) time which turns out to be O(nlogn).
/ Now consider the case where the tree is unbalanced. So, all nodes are on one side like a list. That will give you a height of O(n) but at the same time only one leaf will be present there. So it will give the time complexity as O(n-1 + n), which is O(n). So, the case which turns out to be the worst generally for most tree problems is not the worst case here.
/ By this we can conclude that as the number of leaves increase in the tree, the time complexity moves towards the worst side, as more paths will be generated.
? https://leetcode.com/problems/binary-tree-paths/discuss/68258/Accepted-Java-simple-solution-in-8-lines/562740
"""


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        result = []
        curPath = [str(root.val)]

        def backtracking(root):
            if root.left is None and root.right is None:
                result.append('->'.join(curPath))
                return

            if root.left is not None:
                curPath.append(str(root.left.val))
                backtracking(root.left)
                curPath.pop()

            if root.right is not None:
                curPath.append(str(root.right.val))
                backtracking(root.right)
                curPath.pop()

        backtracking(root)

        return result
