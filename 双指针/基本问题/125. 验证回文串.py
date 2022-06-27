
#* The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False. 或者也可以 isdigit(), isalpha() 一起用
#! 这道题最重要的是确保 s[left] 和 s[right] 进行比较的时候指向的都是「有效的字符」且两个指针没有越界. 保证两个都是「有效的字符」需要〚if〛判断句中的〚continue〛, 否则的话遇到 
#! "a  bbA" 中间有两个「非有效的字符」的情况, 将会直接将 " " 与 "b" 进行比较, 得到错误的结果. 通过〚continue〛确保两个指针在比较时都能指向「有效的字符」. 
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
            # print(s[left], s[right])
            left += 1
            right -= 1
        return True
    
    #* 检查 char 是否是字母或者数字字符
    def letters_digits_check(self, char):
        #! 注意「是字符」的情况可能是在小写范围内或者大写范围内，两者有一成立就返回 True，所以是或者的关系
        letterCheck = 'a' <= char <= 'z' or 'A' <= char <= 'Z'
        digitCheck = '0' <= char <= '9'
        
        return letterCheck or digitCheck
    

Solution().isPalindrome("a  bbA")
