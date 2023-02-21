""" 
! 使用了归并排序中合并两个有序数组的思路
* 可以简单理解为: 同时遍历两个链表，当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

? 链接: https://leetcode.cn/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

/ 时间复杂度: l1 和 l2 链表都遍历了一遍, 那么时间复杂度为 O(n + m). n 和 m 是链表 l1 和 l2 的长度
/ 空间复杂度: 只多申请了一个链表头结点, 常数级别的,  那么空间复杂度 O(1)
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode()
        h1 = list1
        h2 = list2
        cur = tempHead
        while h1 != None or h2 != None:
            # print
            # print(cur.val)
            if h1 == None:
                cur.next = h2
                break
            elif h2 == None:
                cur.next = h1
                break
            elif h1.val < h2.val:
                cur.next = h1
                cur = cur.next
                h1 = h1.next
            else:
                cur.next = h2
                cur = cur.next
                h2 = h2.next

        return tempHead.next
