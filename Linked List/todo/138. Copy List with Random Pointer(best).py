
""" 
? 更细致的图形以及更类似的代码: https://leetcode.cn/problems/copy-list-with-random-pointer/solution/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/
? 宫水三叶以及注释来源: https://leetcode.cn/problems/copy-list-with-random-pointer/solution/gong-shui-san-xie-yi-ti-shuang-jie-ha-xi-pqek/

/ 时间复杂度: O(n)
/ 空间复杂度: O(1)
"""
class Solution(object):
    def copyRandomList(self, head):
        oldListPointer = head
        #* 对原链表的每个节点节点进行复制，并追加到原节点的后面；
        while oldListPointer != None:
            newNode = Node(oldListPointer.val)
            newNode.next = oldListPointer.next
            oldListPointer.next = newNode
            oldListPointer = oldListPointer.next.next
            
        """ 
        * 完成上述操作之后，链表的奇数位置代表了「原链表」节点，链表的偶数位置代表了「新链表」节点，且每个「原节点」的 next 指针指向了对应的「新节点」。这时候，我们需要构造新链表的 random 指针关系，可以利用 link[i + 1].random = link[i].random.next，i 为奇数下标，含义为「新链表」节点的 random 指针指向「原链表」对应节点的 random 指针的下一个值；
        """
        oldListPointer = head
        while oldListPointer != None:
            if oldListPointer.random != None:
                oldListPointer.next.random = oldListPointer.random.next
            oldListPointer = oldListPointer.next.next
        
        #* 对链表进行拆分操作。
        dummyHead = Node(0)
        newListPointer = dummyHead
        oldListPointer = head
        
        while oldListPointer != None:
            newListPointer.next = oldListPointer.next
            oldListPointer.next = oldListPointer.next.next
            newListPointer = newListPointer.next
            oldListPointer = oldListPointer.next
            
        return dummyHead.next
            