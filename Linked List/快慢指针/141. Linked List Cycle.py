""" 
1) 使用 "while fast and fast.next:" 的判别条件就不用单独判断空链表的情况了
2) 使用 "while fast.next and fast.next.next" 的话还需要再对空链表进行特殊判断, 因为判别条件中的 fast.next 会使得程序崩溃

"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # if head == None:
        #     return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
