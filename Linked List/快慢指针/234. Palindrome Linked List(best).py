
#? https://leetcode.cn/problems/palindrome-linked-list/solution/shou-hua-tu-jie-hui-wen-lian-biao-kuai-man-zhi-zhe/

#* 找到中间的那个节点（用快慢指针）。然后对节点后面的做翻转链表，
#* 然后遍历以 头结点 和中点 开始的 后面链表是否相同

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        #* 一开始都指向 head
        slow, fast, prevNodeBeforeMid = head, head, None
        
        #! 用 prevNodeBeforeMid 在下面循环中保存 slow 的前一个结点，之后通过 prevNodeBeforeMid.next = None 断成两个链表。如果没有 prevNodeBeforeMid, 中间节点的前一个节点依然会与中间节点通过 .next 连接，虽然因为 中间节点所在的位置在翻转后成为了尾节点，又因为我们最后比较时使用的判断语句，不影响答题的正确性。但是在这里进行分割是最好的
        #* 利用快慢指针找到中点, 只要每次 fast 比 slow 走快一倍，fast 到终点，那么 slow 到中点
        while fast and fast.next:
            prevNodeBeforeMid = slow
            slow = slow.next
            fast = fast.next.next
        
        if prevNodeBeforeMid:
            prevNodeBeforeMid.next = None
        
        #* 反转链表(方法与 206 一致)，每次只要把当前节点指向上一节点即可
        prev = None

        while slow:
            #* 先用 tmp 保存当前位置的下一个节点的信息，保证单链表不会因为失去下一个节点而就此断裂
            tmp = slow.next 
            slow.next = prev 
            prev = slow 
            slow = tmp

        #* 反转后的链表的头节点就是 prev 所在的位置
        anotherHead = prev
            
        #* 开始比较是否相等
        while head and anotherHead:
            if head.val != anotherHead.val:
                return False
            head = head.next
            anotherHead = anotherHead.next
        
        return True
