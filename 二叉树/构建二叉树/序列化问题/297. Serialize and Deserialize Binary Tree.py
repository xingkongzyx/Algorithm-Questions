"""
# 重要的注意点是为空树时要用 "X" 代替，这样才能先序唯一确定一棵树。如果没有 "X" 表示空树，需要〔先序加中序〕或者〔后序加中序〕才能唯一确定一棵树。强制为空树加上 "X" 表示反而简化了这个问题。
! 选择「前序」遍历，是因为「根|左|右」的打印顺序，在反序列化时更容易定位出根节点的值。
? 必看: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/ 
? 带图片: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/
/ 时间复杂度：在序列化和反序列化函数中, 我们只访问每个节点一次, 因此时间复杂度为 O(n), 其中 n 是节点数, 即树的大小。
/ 空间复杂度：在序列化和反序列化函数中, 我们递归会使用栈空间, 故渐进空间复杂度为 O(n)。

"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # / 递归函数作用: 创建以当前节点node为根节点的子树的序列化字符串
        def DFS(node):
            if node == None:
                return "X"

            leftSubTreeStr = DFS(node.left)
            rightSubTreeStr = DFS(node.right)
            # * 当前节点与其左右子树的序列化结果要使用 "," 进行连接
            curNodeTreeStr = str(node.val) + "," + \
                leftSubTreeStr + "," + rightSubTreeStr

            return curNodeTreeStr

        return DFS(root)

    def deserialize(self, data):

        # / 递归函数作用: 创建以当前 treeList 的首项(treeList[0])为根节点的子树，并返回创建的根节点
        def buildTree(treeList):
            if len(treeList) == 0:
                return None

            poppedVal = treeList.pop(0)
            # * 如果是"X"表示空节点
            if poppedVal == "X":
                return None

            # * 否则创建当前节点作为根节点
            rootNode = TreeNode(int(poppedVal))

            # * 分别创建当前节点的左子树和右子树
            rootNode.left = buildTree(treeList)
            rootNode.right = buildTree(treeList)
            return rootNode

        treeList = [ele for ele in data.split(",") if ele != ""]
        # print(treeList)
        return buildTree(treeList)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
