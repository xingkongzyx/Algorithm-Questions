class Solution:
    def reverseVowels(self, s):
        sList = list(s)
        vowelList = ['a', 'e', 'i', 'o', 'u']
        left = 0
        right = len(sList) - 1
        while left < right:
            if not self.isVowels(sList[left], vowelList):
                left += 1
                continue
            if not self.isVowels(sList[right], vowelList):
                right -= 1
                continue
                
            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
        return "".join(sList)
    
    #* 检查某个字符是否是元音字母
    def isVowels(self, char, vowelList):
        return char.lower() in vowelList

print(Solution().reverseVowels(s = "leetcode"))
