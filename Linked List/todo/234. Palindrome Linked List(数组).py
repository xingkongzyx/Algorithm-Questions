class Solution(object):
    def isPalindrome(self, head):
        stack = []
        
        while head != None:
            if len(stack) == 0:
                stack.append(head.val)
            else:
                topVal = stack[-1]
                if head.val != topVal:
                    stack.pop()
                else:
                    stack.append(head.val)
            head = head.next
            
        return True if len(stack) == 0 else False
