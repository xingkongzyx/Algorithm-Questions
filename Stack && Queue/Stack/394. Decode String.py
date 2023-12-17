""" 
# 碰到 "[" 数字和当前字符串入栈, 碰到 "]" 数字和字符串出栈。
* 以下用 "a2[b]" 举例子: 
*  1 当遇到 '[', 把 '[' 和与之匹配的 ']' 之间的字母需要重复的次数和 '[' 之前的字符进栈, 本例中进栈 (2, "a")
*  2 当遇到 ']', 代码中的字符串res即: b, 就是要重复的字母, 此时出栈之前进栈的(2, "a"), res 变成 a + 2 * b = "abb"

! 外层的解码需要等待内层解码的结果。先扫描的字符还用不上, 但不能忘了它们。所以由内到外, 层层解决[ ], 但是需要保持对外面字符的记忆, 于是用栈。
? 例子链接: https://leetcode.cn/problems/decode-string/solution/zhi-xing-yong-shi-0-ms-zai-suo-you-c-ti-jiao-zh-47/
? 代码: https://leetcode.cn/problems/decode-string/solutions/19447/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
"""


class Solution:
    def decodeString(self, s) -> str:
        multi = 0
        # * 实时记录当前可以提取出来的字符串
        res = ""

        # * (int, str) 记录括号外的上一个数字和之前的字符串
        stack = []
        for char in s:
            if "1" <= char <= "9":
                multi = multi * 10 + int(char)
            elif char == "[":
                stack.append((multi, res))
                multi = 0
                res = ""
            elif char == "]":
                # * 当 char 为 ] 时, stack 出栈, 拼接字符串 res = lastRes + curCharCount * res
                curCharCount, lastRes = stack.pop()
                res = lastRes + res * curCharCount
            else:
                res += char
        # print(res)
        return res


Solution().decodeString(s="3[a2[c]]")
