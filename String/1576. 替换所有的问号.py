""" 
!替换时, 实际不需要遍历所有的小写字母, 只需要遍历三个互不相同的字母, 就能保证一定找到一个与前后字符均不相同的字母, 在此我们可以限定三个不同的字母为 ('a', 'b', 'c')。

/ 时间复杂度: O(C*n), 其中 n 是字符串的长度, 我们需要遍历一遍字符串, C 表示可替代字符的数量, 在本题中 C=3。
/ 空间复杂度: O(1)。除了函数返回值以外我们不需要再申请额外的空间。

? https://leetcode.cn/problems/replace-all-s-to-avoid-consecutive-repeating-characters/solution/ti-huan-suo-you-de-wen-hao-by-leetcode-s-f7mp/
"""


class Solution:
    def modifyString(self, s: str) -> str:
        sList = list(s)
        for i in range(len(sList)):
            if sList[i] == "?":
                prevLetter = sList[i-1] if i > 0 else ''
                nxtLetter = sList[i + 1] if i < len(sList) - 1 else ''
                for char in "abc":
                    if char != prevLetter and char != nxtLetter:
                        sList[i] = char
                        break

        return "".join(sList)
