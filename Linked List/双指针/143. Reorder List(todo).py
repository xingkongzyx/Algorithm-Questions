
#? https://leetcode.cn/problems/reorder-list/solution/dong-hua-yan-shi-kuai-man-zhi-zhen-143-z-4kmk/
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 寻找中心节点
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 对中心节点后的链表进行反转
        # 1->2->3->4->5 变为 1->2->3 以及 5->4
        pre = None
        curNode = slow.next
        slow.next = None
        while curNode != None:
            tempNextNode = curNode.next
            curNode.next = pre
            pre = curNode
            curNode = tempNextNode

        # 1->2->3 以及 5->4 交替插入变为 1->5->2->4->3
        p1 = head
        p2 = pre

        while p1 != None and p2 != None:
            # 因为要更改指向，所以必须提前记录 p1 以及 p2 的 next node
            p1Next = p1.next
            p2Next = p2.next
            
            p1.next = p2
            p2.next = p1Next
            
            p1 = p1Next
            p2 = p2Next
        
        return head
