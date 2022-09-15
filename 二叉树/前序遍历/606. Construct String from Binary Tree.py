""" 
* 前序遍历没什么好说的, 难点在于加括号时区分左右子树。
* 左子树加括号的条件是: 1.左子树不空, 2.左子树为空, 但右子树不空；
* 右子树加括号的条件是: 右子树不空
? 思路: https://leetcode.cn/problems/construct-string-from-binary-tree/solution/qian-xu-bian-li-mei-shi-yao-hao-shuo-de-nan-dian-z/
"""


class Solution:
    def tree2str(self, root) -> str:
        res = []

        def DFS(curNode):
            if curNode == None:
                return

            # * 处理当前 node
            res.append(str(curNode.val))

            # * 如果「左子树」或者「右子树」有任何一个存在, 都需要处理左子树(对应示例2)
            if curNode.left or curNode.right:
                res.append("(")
                DFS(curNode.left)
                res.append(")")

            # * 如果「右子树」存在, 则需要处理右子树。如果不存在, 则不需要处理
            if curNode.right:
                res.append("(")
                DFS(curNode.right)
                res.append(")")

            return

        DFS(root)
        return ''.join(res)
