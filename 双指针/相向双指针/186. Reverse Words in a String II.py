""" 
? https://leetcode.cn/problems/reverse-words-in-a-string-ii/solution/c-python3-shu-zu-fan-zhuan-di-1ci-zheng-0wxxp/
"""


class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseHelper(s, leftIdx, rightIdx):
            while leftIdx < rightIdx:
                s[leftIdx], s[rightIdx] = s[rightIdx], s[leftIdx]
                leftIdx += 1
                rightIdx -= 1

        reverseHelper(s, 0, len(s) - 1)

        leftIdx = 0
        for i in range(len(s)):
            if s[i] == " ":
                # 遇到空格, 翻转前面的单词
                rightIdx = i - 1
                reverseHelper(s, leftIdx, rightIdx)
                leftIdx = i + 1
        # 最后, 翻转最后一个单词
        reverseHelper(s, leftIdx, len(s) - 1)
        return s


print(Solution().reverseWords(
    ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
