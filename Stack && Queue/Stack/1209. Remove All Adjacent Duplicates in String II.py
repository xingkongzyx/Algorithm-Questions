""" 
* 用一个栈模拟，栈中元素为一个 tuple (letter, count)，第一个值为字母，第二个为它的连续重复次数；
? https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/solution/zhan-python3-by-smoon1989/

/ 时间复杂度: O(n)，其中 n 是字符串长度。每个字符只处理一次。
/ 空间复杂度: O(n)，栈空间。
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []

        for char in s:
            # * 如果栈为空，直接加入
            if len(stack) == 0:
                stack.append((char, 1))
            else:
                # * 提取栈顶的 tuple
                peekEle, peekEleTimes = stack[-1]
                # * 如果栈顶的元素不等于当前遍历到的字符, 直接将当前遍历到的字符以及其其出现次数 1, 作为 tuple 放入 stack
                if peekEle != char:
                    stack.append((char, 1))
                else:
                    # * 如果「栈顶元素」等于当前遍历到的字符. 并且如果「栈顶元素」出现次数加上当前遍历到的一次等于 k, 则将栈顶元素弹出. 否则只需更新「栈顶元素」的出现次数(因为 tuple是 immutable, 所以采取 pop 然后 append 一个新的 tuple 对的方式)
                    if peekEleTimes + 1 == k:
                        stack.pop()
                    else:
                        stack.pop()
                        stack.append((peekEle, peekEleTimes + 1))

        res = ""

        for char, times in stack:
            res += char * times

        return res


Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2)
