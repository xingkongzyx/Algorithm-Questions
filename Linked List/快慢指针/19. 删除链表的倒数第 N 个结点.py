
#? 图片: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/dong-hua-yan-shi-19-shan-chu-lian-biao-de-dao-shu-/
#? https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/hua-jie-suan-fa-19-shan-chu-lian-biao-de-dao-shu-d/
""" 
* 假设链表如下: p->1->2->3->4->5
* p是哨兵指针, slow(简写为s) 和 fast(简写为f) 初始时都指向 p, n=2

* f 先走两步后指向 2, 如下: 
* p->1->2->3->4->5
*       f

* 之后, s 和 f 再一起前进. 
* 假设判断条件改成了 while f, 那么这一趟执行完后, f 就指向空了, 也就是前进了 4 位, 而 s 也要相应的前进 4 位:
* p->1->2->3->4->5->None
*             s       f
* 最后再执行 slow.next = slow.next.next 结果就不对了, 因为 fast 多前进了一位。
"""
def removeNthFromEnd(self, head, n):

    #* 虚拟头节点
    dummyHead = ListNode()
    dummyHead.next = head  #! 最后用于返回,防止删除的是head

    #* 前后指针分别指向dummyHead, 然后间隔n
    slow,fast = dummyHead,dummyHead
    #* fast向前走n步
    while n>0:
        fast= fast.next
        n -= 1       
    #* 当fast走到头时, slow刚好处于倒数第N-1个节点
    while fast.next:
        slow = slow.next
        fast = fast.next
    #* 覆盖掉slow的next节点, 即删除第n个节点
    slow.next = slow.next.next 
    
    #* 由于预置了节点, 所以slow.next必然存在(为head), 即使只有一个节点,slow.next.next 为 None, 也是符合条件的. 这里返回预设指针的下一个节点
    return dummyHead.next 
