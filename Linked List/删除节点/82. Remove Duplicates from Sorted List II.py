
""" 
! 区别在于:  83题中重复的元素会保留一个 而本题中重复的元素不保留
#* 循环不变量 [dummyHead, slow] 左闭右闭区间内的「链表节点」都是链表中「不存在重复」的节点, slow.next 指向下一个链表中可能「不存在重复」的节点

* 双指针, 一次遍历
* 判断「快指针」所在位置的节点的值与「快指针的 next指针」指向节点的值是否相等, 相等则 fast = fast.next; 这其中又能分两种情况讨论: 
* ➊ 如果上述操作结束后快慢指针是相邻的: 说明他们之间没有『重复区域』, slow 可以向后移动, slow = slow.next 依旧满足循环不变量的定义. exp: 1->2->3
* ➋ 快慢指针不相邻: 说明快慢指针间出现了『重复区域』, 上述操作结束后 fast.next 「可能是」「不存在重复」的节点, 但只是「可能」。所以只更新 slow.next 的指向, 跳过重复区域, 但 slow 本身不会改变. 只有再出现情况 ➊ 时 slow本身 才会向后移动, 因为我们的循环不变量是 "[dummyHead, slow] 左闭右闭区间内的「链表节点」都是链表中「不存在重复」的节点", 必须确保 slow 目前的节点是「不存在重复」的节点

https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solution/fu-xue-ming-zhu-di-gui-die-dai-yi-pian-t-wy0h/
https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solution/python3-shuang-zhi-zhen-by-littlelion_njuer-2/
"""
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        
        slow = dummyHead
        fast = head
        
        while fast != None:
            #* 如果有相同的节点, 那么 fast 指针需要向后移动, 直到 fast.next 是空 或者 fast.next 是一个新的元素, 而 [slow.next, fast] 闭区间内的所有节点都是重复的
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            
            #* 正如上面提到的 [slow.next, fast] 闭区间内的所有节点都是重复的, 如果这个区间只有一个值, 说明 slow.next 这个元素不是重复元素, 可以保留, slow 向后移动, 依旧符合 循环不变量是 "[dummyHead, slow] 左闭右闭区间内的「链表节点」都是链表中「不存在重复」的节点"
            if slow.next == fast:
                slow = slow.next
            else:
            #* 这个时候 [slow.next, fast] 闭区间内的所有节点都是重复的, 要越过这些节点, 所以让 slow.next = fast.next. 但此时并不能确定 fast.next 对应的元素是否是重复节点, 为了保持循环不变量的定义, 此时不移动 slow 指针
                slow.next = fast.next
            fast = fast.next
        return dummyHead.next
            
