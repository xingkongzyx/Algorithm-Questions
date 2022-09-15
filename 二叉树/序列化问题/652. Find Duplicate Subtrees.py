""" 
* 要解决以当前节点为根的二叉树长什么样, 就得用序列化它的结构. 前序或者后序遍历最是佳的方式。中序不可以！！
* 要知道以其它节点为根的二叉树长什么样, 就得把二叉树结构序列化的结果存储起来
* 总的来说: 既然我们要找重复的子树, 那么我们只需要将所有子树都使用相同的方式进行序列化, 那在此过程中如果发现有相同的序列, 那我们就可以找出相同的子树。

? 为什么不能采用中序遍历呢? https://leetcode.cn/problems/find-duplicate-subtrees/solution/by-muse-77-lsy1/

? 综合性讲解: https://leetcode.cn/problems/find-duplicate-subtrees/solution/652-xun-zhao-zhong-fu-de-zi-shu-by-ming-zhi-shan-y/
? 代码清晰: https://leetcode.cn/problems/find-duplicate-subtrees/solution/hou-xu-bian-li-xu-lie-hua-hashcun-chu-by-k940/
/ 时间复杂度: DFS 过程复杂度为 O(n)，对于每个子树需要构造出与子树同等规模的字符串，复杂度为 O(n)。整体复杂度为 O(n^2)
/ 空间复杂度: O(n)

"""


class Solution:
    def findDuplicateSubtrees(self, root):
        # 使用哈希表记录每个子树的出现次数, 当出现次数为 2（首次判定为重复出现）时, 将该节点加入答案。
        record = {}
        res = []
        """ 
        / 递归函数的作用: 将以 node 为根节点的子树进行序列化, 并返回序列化的字符串结果
        / 递归函数的输入: 根节点
        / 递归函数的输出: 序列化后的字符串结果
        """
        def DFS(node):
            if node == None:
                return ""

            # * 将左右子树序列化成字符串, 当前节点加上左右子树, 就是以自己为根的二叉树序列化结果
            treeStr = str(node.val) + "(" + DFS(node.left) + ")" + \
                "(" + DFS(node.right) + ")"

            record[treeStr] = record.get(treeStr, 0) + 1
            # * 只有当 treeStr 正好「第二次」出现的时候才将其加入结果 res, 之后即使再出现因为已经加入过 res 便不再理会, 避免「重复的根节」点出现在 res 中
            if record[treeStr] == 2:
                res.append(node)
            return treeStr

        DFS(root)
        print(res)
        return res
