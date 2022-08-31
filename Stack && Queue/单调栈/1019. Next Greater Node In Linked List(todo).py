""" 
? https://leetcode.cn/problems/next-greater-node-in-linked-list/solution/10xing-dai-ma-biao-zhun-by-huxiyue-bqjl/
/ 时间复杂度 O(N): 每个节点出栈入栈一次)
/ 空间复杂度O(N): 栈空间
"""


class Solution:
    def nextLargerNodes(self, head):
        ans = []
        currentNode = head
        stack = []
        # * 需要记录元素对应到ans中的下标。
        i = 0

        while currentNode:
            while stack and stack[-1][1] < currentNode.val:
                ans[stack[-1][0]] = currentNode.val
                stack.pop()
            # * stack 中存储的是一个pair - (链表中的元素的值, 链表中的元素的位置(索引)), 这样便于修改下标
            stack.append((i, currentNode.val))
            # * ans 无论在什么情况下都需要添加元素，从而确保遍历结束后还没有找到 next greater node 的节点也有默认的结果值 0
            ans.append(0)
            i += 1
            currentNode = currentNode.next
        return ans
