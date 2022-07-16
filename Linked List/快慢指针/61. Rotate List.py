""" 
* 假设链表的长度为n, 为了将链表每个节点向右移动 k 个位置, 我们只需要将链表的后 「k % n」个节点移动到链表的最前面, 然后将链表的后「k % n」个节点和前「n - k」个节点连接到一块即可。
? 链接：https://leetcode.cn/problems/rotate-list/solution/xuan-zhuan-lian-biao-tu-jie-lian-biao-zu-ku33/
? https://leetcode.cn/problems/rotate-list/solution/ji-bai-liao-91de-javayong-hu-qing-xi-yi-dong-by-re/
"""
class Solution(object):
    def rotateRight(self, head, k):
        #* 特殊情况判断
        if head == None or k == 0:
            return head
        
        #* 求出链表的长度 n
        length = 0
        tempHead = head
        
        while tempHead != None:
            length += 1
            tempHead = tempHead.next

        k = k % length
        
        #* 特殊情况判断
        if k == 0:
            return head
        
        #* 通过「19. 删除链表的倒数第N个节点」的『快慢指针』的思路设置 slow, fast 两个指针指向 head, 并且 fast 提前移动 k 位, 这样当 fast.next == None 时, fast 指向链表的最后一个节点, 因为 fast 比 slow 领先 k 个位置, 此时 slow 指向链表的旋转点的前一位, 数学表达就是 length - k 的位置(index 1 开始算)
        slow = head
        fast = head
        while k > 0:
            fast = fast.next
            k -= 1
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        #* 记录返回值的头结点
        newHead = slow.next
        #* 断开连接
        slow.next = None
        #* 后一段的末尾指向原来的开头
        fast.next = head
        return newHead
