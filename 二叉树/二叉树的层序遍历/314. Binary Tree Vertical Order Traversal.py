""" 
* 实现垂直顺序, 可以用加下标的方式表示这棵树。需要注意的是, 应该使用BFS, 保证「深度较小」的节点最先被遍历。如何保证按照「垂直顺序」组织答案? 我们维护一个queue用来记录当前节点的index。index遇到左子树减一, 右子树加一。另外维护一个minIdx, 用来最后输出结果时作为最左子树的起始下标。

* 在遍历的时候, 需要附带位置信息, 根据位置信息来组织答案: 使用一个哈希表: rec<当前节点的index, 该位置的结点值列表>
? 代码借鉴: https://leetcode.cn/problems/binary-tree-vertical-order-traversal/solution/c-ceng-xu-bian-li-you-xu-hash-by-sptuan/ 的评论、
? 简练好理解: https://leetcode.cn/problems/binary-tree-vertical-order-traversal/solution/ceng-xu-bian-li-jian-ji-yi-dong-de-ti-ji-33iq/
/ 时间复杂度: O(N) N为结点数。
/ 空间复杂度: O(N) N为结点数。
"""


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict, deque
        if root == None:
            return []

        queue = deque([])
        queue.append([root, 0])
        rec = defaultdict(list)
        minIdx = float("inf")

        while queue:
            levelNodesNum = len(queue)

            for _ in range(levelNodesNum):
                curNode, curNodeIdx = queue.popleft()
                minIdx = min(minIdx, curNodeIdx)
                rec[curNodeIdx].append(curNode.val)

                if curNode.left:
                    queue.append([curNode.left, curNodeIdx - 1])

                if curNode.right:
                    queue.append([curNode.right, curNodeIdx + 1])
        res = []

        # * 记录了 rec 中 key 的最小值才能够正确的遍历 rec
        for i in range(minIdx, minIdx + len(rec)):
            res.append(rec[i])

        return res
