
""" 
* 我们可以将此题分为3个步骤: 
* 
* ① 利用快慢指针找到链表的中心点
* ② 将链表的后半部分反转
* ③ 然后将反转的后半部分插入前半部分
?https://leetcode.cn/problems/reorder-list/solution/dong-hua-yan-shi-kuai-man-zhi-zhen-143-z-4kmk/

"""


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # * ① 利用快慢指针找到链表的中心点
        slow = head
        fast = head

        # # 使用这样的判别条件在节点个数为偶数个时取到的是左边的节点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # * ② 将链表的后半部分反转
        # * 奇数个节点: 1->2->3(mid)->4->5 变为 1->2->3(mid) 以及 5->4
        # * 偶数个节点: 1->2->3(mid)->4->5->6 变为 1->2->3(mid) 以及 6->5->4
        pre = None
        curNode = slow.next

        # * 将原来的链表在 midNode 处断开, 此时链表变成 [head-> ... -> midNode(slow)] 和 [midNode.next(curNode)-> ... -> tail] 两部分, 我们翻转第二部分
        slow.next = None
        while curNode != None:
            tempNextNode = curNode.next
            curNode.next = pre
            pre = curNode
            curNode = tempNextNode

        # * ③ 然后将反转的后半部分插入前半部分
        p1 = head
        p2 = pre

        while p1 != None and p2 != None:
            # * 因为要更改指向, 所以必须提前记录 p1 以及 p2 的 next node
            p1Next = p1.next
            p2Next = p2.next

            p1.next = p2
            p2.next = p1Next

            p1 = p1Next
            p2 = p2Next

        return head
