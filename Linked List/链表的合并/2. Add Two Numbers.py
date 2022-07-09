""" 
* 根据题意可知链表数字位数是从小到大的
* 
* ➀ 因为两个数字相加会产生进位, 所以使用 carry 来保存进位。
* ➁ 则当前位的值为(l1.val + l2.val + carry) % 10
* ➂ 则进位值为(l1.val + l2.val + carry) / 10
* ➃ 建立新node, 然后将进位传入下一层。

/ 时间复杂度: O(max(m,n))
/ 空间复杂度: O(max(m,n))
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        #* 定义一个进位数变量, 用来存储当两数之和大于10的时候的进位
        carry = 0
        
        #* 定义一个新联表伪指针, 用来指向头指针, 方便返回结果
        dummyHead = ListNode(0)
        #* 定义一个可移动的指针, 用来指向存储两个数之和的位置
        tempHead = dummyHead
        
        l1Head = l1
        l2Head = l2
        
        #* 当l1 不等于null或l2 不等于空时, 就进入循环
        while l1Head != None or l2Head != None:
            if l1Head == None:
                nodeVal = (l2Head.val + carry) % 10
                carry = (l2Head.val + carry) // 10
                l2Head = l2Head.next
            elif l2Head == None:
                nodeVal = (l1Head.val + carry) % 10
                carry = (l1Head.val + carry) // 10
                l1Head = l1Head.next
            else:
                nodeVal = (l1Head.val + l2Head.val + carry) % 10
                carry = (l1Head.val + l2Head.val + carry) // 10
                l1Head = l1Head.next
                l2Head = l2Head.next
            
            newNode = ListNode(nodeVal)
            tempHead.next = newNode
            tempHead = tempHead.next
        
        #* 如果最后两个数, 相加的时候有进位数的时候, 就将进位数, 赋予链表的新节点。
        if carry != 0:
            newNode = ListNode(1)
            tempHead.next = newNode
            tempHead = tempHead.next
        return dummyHead.next 
