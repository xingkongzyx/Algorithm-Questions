
#* The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False. 或者也可以 isdigit(), isalpha() 一起用
class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
            
            # print(s[left].upper(), s[right].upper())
            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True
res = Solution().isPalindrome("0P")
print(res)
