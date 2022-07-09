
#? https://leetcode.cn/problems/delete-node-in-a-linked-list/solution/tu-jie-shan-chu-lian-biao-zhong-de-jie-dian-python/
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
