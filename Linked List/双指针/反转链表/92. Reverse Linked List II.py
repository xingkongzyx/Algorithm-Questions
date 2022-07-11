""" 
* 第一步：找到待反转节点的前一个节点. 
* 第二步：反转 left 到 right 这部分. 『使用 206 的思路』
* 第三步：将反转的起点的 next 指向反转的后面一部分. 
* 第四步：将第一步找到的节点指向反转以后的头节点. 

? https://leetcode.cn/problems/reverse-linked-list-ii/solution/ji-bai-liao-100de-javayong-hu-by-reedfan-6/

"""

class Solution(object):
    def reverseBetween(self, head, left, right):
        dummyHead = ListNode(0)
        dummyHead.next = head
        count = 1
        before = dummyHead

        #* 第一步：找到待反转节点的前一个节点. count = 1 时 before 对应的是「虚拟头节点」而不是 head, 所以当 count == left 时 before 对应的是待反转节点的前一个节点 
        while count < left:
            before = before.next
            count += 1
        
        #* 第二步：反转 left 到 right 这部分链表, 方法与『206 的思路』一样, 使用双指针法, 设置一个 pre 节点, 一个 cur 节点
        prev = None
        current = before.next

        count = left
        #* 『count == right』时 cur 指向 right 位置的节点, 这也是最后一个待翻转的节点
        while count <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            count += 1
            
        ## 翻转以后, prev 指向链表中的 right 位置, cur 指向 right 位置的下一个节点
        #* 第三步：将反转部分的尾节点(通过 before.next 获取)的 next 指向反转的后面一部分(cur 所在位置). 
        before.next.next = current
        #* 第四步：将第一步找到的 before 节点的 next 指向反转部分的新的头节点(也就是 prev 在的位置). 
        before.next = prev
        return dummyHead.next
