""" 
* 因为题目要求是在「两个中间结点」的时候，返回『第二个中间结点』。所以快指针可以前进的条件是: 当前快指针和当前快指针的下一个结点都非空。
* 如果题目要求在「两个中间结点」的时候，返回『第一个中间结点』，此时快指针可以前进的条件是: 当前快指针的下一个结点和当前快指针的下下一个结点都非空。
# 上面讲述的其实就是对应两种 while 判断形势 while(fast && fast.next) 或者 while(fast.next && fast.next.next)
? https://leetcode.cn/problems/middle-of-the-linked-list/solution/kuai-man-zhi-zhen-zhu-yao-zai-yu-diao-shi-by-liwei/
"""


class Solution(object):
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
