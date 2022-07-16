
#? 图片的讲解: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/solution/83-shan-chu-pai-xu-lian-biao-zhong-de-zhong-fu-21/ 
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        
        validPointer = head
        traversePointer = head.next

        #* 循环不变量 [head, validPointer] 左闭右闭区间中的链表节点都是不重复的, validPointer.next 指向下一个「不重复」的节点

        while traversePointer != None:
            if traversePointer.val == validPointer.val:
                validPointer.next = traversePointer.next
            else:
                validPointer = validPointer.next
            traversePointer = traversePointer.next
        
        #* 因为定义是到 validPointer 为止的节点都是不重复的，traversePointer 为 null 结束循环整个链表后，[head, validPointer] 之间就已经包括了链表中所有不重复的节点。此时只需要让 validPointer.next 指向 None 结束链表即可
        validPointer.next = None
        return head

