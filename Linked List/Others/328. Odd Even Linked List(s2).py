
#? https://leetcode.cn/problems/odd-even-linked-list/solution/shou-hua-tu-jie-328qi-ou-lian-biao-odd-even-linked/
class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return None
        
        oddHead = head
        evenHead = head.next
        tempEvenHead = evenHead
        while tempEvenHead and tempEvenHead.next:
            oddHead.next = tempEvenHead.next
            oddHead = oddHead.next
            
            tempEvenHead.next = oddHead.next
            tempEvenHead = tempEvenHead.next
        oddHead.next = evenHead    
        return head
