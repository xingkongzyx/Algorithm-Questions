""" 
? https://leetcode.cn/problems/odd-even-linked-list/solution/kuai-lai-wu-nao-miao-dong-qi-ou-lian-biao-by-sweet/
/ 时间复杂度: O(n), 其中 n 是链表的节点数。需要遍历链表中的每个节点, 并更新指针。
/ 空间复杂度: O(1)。只需要维护有限的指针。
"""
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddDummyHead = ListNode(-1)
        evenDummyHead = ListNode(-2)
        
        tempOddHead = oddDummyHead
        tempEvenHead = evenDummyHead

        cur = head
        i = 1
        #* 遍历原链表, 根据 i 是奇数还是偶数决定将当前结点插入到奇链表还是偶链表
        while cur != None:
            if i % 2 == 1:
                tempOddHead.next = cur
                tempOddHead = tempOddHead.next
            else:
                tempEvenHead.next = cur
                tempEvenHead = tempEvenHead.next
            cur = cur.next
            i += 1
        #* 如果链表中只有偶数个节点, 则最后的 tempEvenHead 指针的 next 指向 null, 可如果链表中有奇数个节点, tempEvenHead 指针的 next 循环结束后依旧指向最后一个节点, 所以需要将其手动变为 null。例子就是题目中的 [1,2,3,4,5] 可以通过打印进行测试
        tempEvenHead.next = None
        #* 最后, 将偶链表拼接在奇链表后面。
        tempOddHead.next = evenDummyHead.next

        return oddDummyHead.next
