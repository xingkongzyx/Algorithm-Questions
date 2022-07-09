class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        result = head
        slow = head
        fast = head

        #* 循环不变量 [result, slow] 左闭右闭区间的链表节点都是不重复的, slow.next 指向下一个不重复的节点

        while fast != None:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        #* 因为定义是到 slow 为止的节点都是不重复的，fast 为 null 结束循环整个链表后，[result, slow] 之间就已经包括了链表中所有不重复的节点。此时只需要让 slow.next 指向 None 结束链表即可
        slow.next = fast
        return result

