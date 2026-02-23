""" 
? 使用官解的解法2: https://leetcode.cn/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if strs == None or len(strs) == 0:
            return ""

        count = len(strs)
        # * 使用 strs[0] 当作标准字符串, 用后面的字符串与它进行比较
        standardStr = strs[0]

        for standardCharIdx in range(len(standardStr)):
            standardChar = standardStr[standardCharIdx]
            # * 用来自 strs[1], strs[2] ... strs[n] 的纵方向平行字符与 standardChar 进行比较
            for strIdx in range(1, count):
                curStr = strs[strIdx]
                # * 如果出现了标准字符串当前的字符指针对应当前字符串 curStr 是越界的 或者 标准字符与当前字符串同一位置的字符不相同, 说明common Prefix 就是 standardStr[0, standardCharIdx - 1], 之所以"-1"是因为当前字符不满足要求
                if standardCharIdx == len(curStr) or standardChar != curStr[standardCharIdx]:
                    return standardStr[:standardCharIdx]

        # * 如果退出了循环还没有返回, 说明 standardStr 是最长的 common Prefix
        return standardStr
