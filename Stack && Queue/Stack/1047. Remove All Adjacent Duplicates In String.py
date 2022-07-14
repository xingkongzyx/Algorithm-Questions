class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            #* 如果 stack 是空的，直接加入当前的char
            if len(stack) == 0:
                stack.append(char)
            else:
                # * 否则与「栈顶元素」进行比较，如果相同，说明这两个就是题目中要消除的 adjacent Duplicates In String，将「栈顶元素」pop 出栈
                peekEle = stack[-1]
                if peekEle == char:
                    stack.pop()
                else:
                    stack.append(char)

        return "".join(stack)
