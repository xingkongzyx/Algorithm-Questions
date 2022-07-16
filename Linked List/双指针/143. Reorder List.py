
""" 
* 我们可以将此题分为3个步骤：
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
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #* ② 将链表的后半部分反转
        #* 奇数个节点: 1->2->3(mid)->4->5 变为 1->2->3(mid) 以及 5->4
        #* 偶数个节点: 1->2->3->4(mid)->5->6 变为 1->2->3->4(mid) 以及 6->5
        
        ## 我们这样设计的原因就是 "避免链表的元素有奇数或偶数个的不同情况", 如果我们直接从「中间节点」处进行翻转, 「偶数个节点」时程序可以顺利运行, 但是当「奇数个节点」时, 后半部分会比前半部分多一个节点, 在我们 "③ 将反转的后半部分插入前半部分" 这一步骤时明明 p2 后面还有元素, 但是 p2.next = p1Next 这一句话让 p2.next 指向了 None, 造成总体缺少了元素. 像 [1,2,3,4,5] 前半部分: [1,2] 后半部分 [5,4,3], 运行后续代码的结果是 [1,5,2,4], 节点 3 丢失。
        ## 为了避免这一错误, 我们让前半部分在「奇数个节点」时比后半部分多「一个」元素, 在「偶数个节点」时比后半部分多「两个」元素, 而我们又会发现「偶数个节点」中间两个节点最后还是会连在一起。像 [1,2,3,4,5,6] 最后变成 [1,6,2,5,3,4], [1,2,3,4] [6,5] 交替插入, 当 p2 为 null 时提前退出循环, 中间的两个节点 3 和 4 还是连载一起的, 程序依旧正确。

        pre = None
        curNode = slow.next
        
        #* 将原来的链表在 midNode 处断开, 此时链表变成 [head-> ... -> midNode(slow)] 和 [midNode.next(curNode)-> ... -> tail] 两部分, 我们翻转第二部分
        slow.next = None
        while curNode != None:
            tempNextNode = curNode.next
            curNode.next = pre
            pre = curNode
            curNode = tempNextNode

        #* ③ 然后将反转的后半部分插入前半部分
        p1 = head
        p2 = pre

        while p1 != None and p2 != None:
            #* 因为要更改指向, 所以必须提前记录 p1 以及 p2 的 next node
            p1Next = p1.next
            p2Next = p2.next
            
            p1.next = p2
            p2.next = p1Next
            
            p1 = p1Next
            p2 = p2Next
        
        return head
