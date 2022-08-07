class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        def DFS(currentNode, parentNode, val, depth):
            if currentNode.val == val:
                return [parentNode, depth]

            if currentNode.left:
                leftCheck = DFS(currentNode.left, currentNode, val, depth + 1)
                if leftCheck:
                    return leftCheck

            if currentNode.right:
                rightCheck = DFS(currentNode.right, currentNode, val, depth + 1)
                if rightCheck:
                    return rightCheck
            return None

        xDFS_result = DFS(root, None, x, 0)
        yDFS_result = DFS(root, None, y, 0)

        if xDFS_result != None and yDFS_result != None \
            and xDFS_result[1] == yDFS_result[1] and \
                xDFS_result[0] != yDFS_result[0]:
            return True
        return False

root = TreeNode(1)
l1 = TreeNode(2)
l2 = TreeNode(4)
r1 = TreeNode(3)
r2 = TreeNode(5)

root.left = l1
l1.right = l2
root.right = r1
r1.right = r2
s =  Solution()
res = s.isCousins(root, 2,5)
print(res)