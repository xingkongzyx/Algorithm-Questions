""" 
时间复杂度：O(n)，n是节点的个数，最差情况下遍历所有节点。

空间复杂度：O(n)，栈的深度，最坏情况下二叉树退化为链表形状。
https://leetcode.cn/problems/cousins-in-binary-tree/solution/shu-ju-jie-gou-he-suan-fa-bfsjie-jue-by-yysyr/
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 
递归函数和参数: 传入parentNode, currentNode, x, y
递归终止条件: 如果这个node是None，则直接返回
本层递归: 前序遍历 首先判断这个node是否是x或者y, 并更新对应的x_depth, y_depth, x_parent, y_parent. 然后分别进行左、右子树遍历

"""
class Solution(object):
    def isCousins(self, root, x, y):
        self.x_depth, self.y_depth, self.x_parent, self.y_parent = None, None, None, None

        def DFS(currentNode, parentNode, x, y, depth):
            if currentNode == None:
                return
            ##中
            
            #/ 如果找到了x节点，就把他的父节点和深度记录下来
            if currentNode.val == x:
                self.x_depth = depth
                self.x_parent = parentNode
            #/ 如果找到了y节点，就把他的父节点和深度记录下来
            elif currentNode.val == y:
                self.y_depth = depth
                self.y_parent = parentNode
            
            #/如果确定他俩是堂兄弟节点了，直接返回，不用再往下遍历了
            if self.x_depth == self.y_depth and self.x_parent != self.y_parent:
                return
            ##左
            DFS(currentNode.left, currentNode, x, y, depth + 1)
            ##右
            DFS(currentNode.right, currentNode, x, y, depth + 1)
            return
        DFS(root, None, x, y, 0)

        #/ 如果他俩的深度一样，也就是在同一层，又不是同一个父亲，那么他俩就是堂兄弟节点，否则不是
        if self.x_depth == self.y_depth and self.x_parent != self.y_parent:
            return True
        return False


root = TreeNode(3)
lnode1 = TreeNode(5)
lnode2 = TreeNode(6)
lnode3 = TreeNode(2)
lnode4 = TreeNode(7)
lnode5 = TreeNode(4)

rnode1 = TreeNode(1)
rnode2 = TreeNode(0)
rnode3 = TreeNode(8)

root.left = lnode1
lnode1.left = lnode2
lnode1.right= lnode3
lnode3.left = lnode4
lnode3.right = lnode5

root.right = rnode1
rnode1.left = rnode2
rnode1.right = rnode3

s =  Solution()
res = s.isCousins(root, 4,5)
print(res)