class Solution(object):
    def reverseString(self, s):      
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right] ,s[left]
            left += 1
            right -= 1
        # print("".join(s))  
        return s

Solution().reverseString(s = ["h","e","l","l","o"])
