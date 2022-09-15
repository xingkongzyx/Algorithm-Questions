
# > 使用与 297 同样的解法
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def DFS(node):
            if node == None:
                return "X"

            leftSubTreeStr = DFS(node.left)
            rightSubTreeStr = DFS(node.right)

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
            # * 如果是"#"表示空节点
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
