""" 
? https://leetcode.cn/problems/reverse-words-in-a-string/solution/yi-ci-bian-li-shi-xian-fan-zhuan-zi-fu-c-cmos/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        # * 因为题目中说: There is at least one word in s. 所以 left right 不会重合的, 可以省略 left < right 的判断
        while left < right and s[left] == " ":
            left += 1

        while left < right and s[right] == " ":
            right -= 1

        # * 唯一的额外空间
        res = []
        while left <= right:
            index = right
            while index >= left and s[index] != " ":
                index -= 1

            # * 现在 index 已经找到了第一个空格，或者此时 index 位于数组的 -1 位置，而 [index+1, right] 就是单词的位置
            res.append(s[index + 1: right + 1])

            # * 如果不是最后的单词，添加空格
            if index > left:
                res.append(" ")

            while index >= left and s[index] == " ":
                index -= 1
            right = index
        return ''.join(res)
