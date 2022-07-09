
#? https://leetcode.cn/problems/palindrome-linked-list/solution/c-shi-yong-shu-zu-fan-zhuan-lian-biao-by-zuo-10/

# 找到中间的那个节点（用快慢指针）。然后对节点后面的做翻转链表，
# 然后遍历以 头结点 和中点 开始的 后面链表是否相同

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow, fast = head, head # 一开始都指向 head
        # 利用快慢指针找到中点, 只要每次fast只slow走快一倍，fast到终点，那么slow到中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 反转链表，每次只要把当前节点指向上一节点即可
        last = slow 
        cur_node = slow.next # 当前位置
        while cur_node:
            tmp = cur_node.next # 先用tmp保存当前位置的下一个节点的信息，
            # 保证单链表不会因为失去下一个节点而就此断裂
            cur_node.next = last # 当前节点指针指向上一个节点
            last = cur_node # 当前节点成为了上一个节点

            cur_node = tmp  # 继续遍历
        # 遍历完之后记得把反转链表的头结点的next置空,否则就会出错
        slow.next = None
            
        # 开始比较是否相等
        while head and last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
        return True
