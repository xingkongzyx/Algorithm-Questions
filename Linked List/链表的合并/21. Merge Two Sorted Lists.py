""" 
* 可以简单理解为: 同时遍历两个链表，当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

? 链接：https://leetcode.cn/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

/ 时间复杂度: l1 和 l2 链表都遍历了一遍, 那么时间复杂度为 O(n + m). n 和 m 是链表 l1 和 l2 的长度
/ 空间复杂度: 只多申请了一个链表头结点, 常数级别的,  那么空间复杂度 O(1)
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummyHead = ListNode(0)
        tempHead = dummyHead
        
        while list1 != None and list2 != None:
                if list1.val < list2.val:
                    tempHead.next = list1           
                    list1 = list1.next
                else:
                    tempHead.next = list2        
                    list2 = list2.next
                tempHead = tempHead.next
        
        if list1 == None:
                tempHead .next = list2
        elif list2 == None:
                tempHead.next = list1
        return dummyHead.next

