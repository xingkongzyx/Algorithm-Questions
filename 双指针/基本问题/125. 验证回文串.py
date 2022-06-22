
#* The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False. 或者也可以 isdigit(), isalpha() 一起用
class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left <= right:
            #* 对于非数字字母的字符跳过判断
            if not self.letters_digits_check(s[left]):
                left += 1
                continue
            
            #* 对于非数字字母的字符跳过判断
            if not self.letters_digits_check(s[right]):
                right -= 1
                continue

            if s[left].upper() != s[right].upper():
                return False
            
            left += 1
            right -= 1
        return True
    
    #* 检查 char 是否是字母或者数字字符
    def letters_digits_check(self, char):
        #! 注意「是字符」的情况可能是在小写范围内或者大写范围内，两者有一成立就返回 True，所以是或者的关系
        letterCheck = 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        digitCheck = '0' <= char <= '9'
        
        return letterCheck or digitCheck
    
