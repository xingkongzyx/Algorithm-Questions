class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 
具体思路如下：
因为在BFS中，我们使用的是层序遍历，如果每次遍历一层，那么这一层的元素的深度是相同的。

因此我们在每一层，看看是否有出现 x 和 y，其中分为以下三种情况：
    1. x 和 y 都没出现 → 那只能往下一层继续找了
    2. x 和 y 只出现一个 → 两个元素的深度不同，不可能为兄弟，返回false
    3. x 和 y 都出现了，好耶，但是还不够好
        3.1 x 和 y 父节点相同 → 不是堂兄弟，是亲兄弟，不行，返回false
        3.2 x 和 y 父节点不同 → 满足题目条件了，好耶，返回true

作者：qian2
链接：https://leetcode.cn/problems/cousins-in-binary-tree/solution/c-you-ya-bfs-by-qiank-9vk9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution(object):
    def isCousins(self, root, x, y):
        if root == None:
            return False
        
        from collections import deque

        #* 第一个元素记录指向当前结点的指针，第二个元素记录指向当前结点的父结点的指针，
        queue = deque([[root, None]])

        while len(queue):
            #* 对同一层的node进行遍历以及判断
            numOfCurrentLevelNodes = len(queue)
            #* x_Check 和 y_Check 用于检查这一层(同意深度)是否包含x和y, 如果包含则它们俩的值在本层的BFS遍历后不应该为None
            x_Check = None
            y_Check = None
            for _ in range(numOfCurrentLevelNodes):
                [poppedNode, parentNode] = queue.popleft()

                if poppedNode.val == x:
                    x_Check = [poppedNode, parentNode]

                elif poppedNode.val == y:
                    y_Check = [poppedNode, parentNode]

                #* 将不为None的左右child node 加入queue，用于下一轮对下面这一层的遍历
                if poppedNode.left:
                    queue.append([poppedNode.left, poppedNode])
                
                if poppedNode.right:
                    queue.append([poppedNode.right, poppedNode])
            #* 最后判断是否 x_Check and y_Check 都不为 None，并且它们俩的parent是不一样的，如果满足条件直接返回True
            if x_Check and y_Check and x_Check[1] != y_Check[1]:
                # print(f"current node val is {x_Check[0].val}, parent val is {x_Check[1].val}")
                # print(f"current node val is {y_Check[0].val}, parent val is {y_Check[1].val}")
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
res = s.isCousins(root, 4,5)
print(res)


            

            