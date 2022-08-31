""" 
? 思路1: https://leetcode.cn/problems/basic-calculator-ii/solution/xian-cheng-chu-zai-jia-jian-yong-zhan-ba-hplr/
? 思路2: https://leetcode.cn/problems/basic-calculator-ii/solution/zui-hou-du-bian-cheng-zuo-jia-fa-leetcod-oxx9/
"""


class Solution:
    def calculate(self, s: str) -> int:
        # * 当前遇到的数字
        curNum = 0
        # * 栈。解析过的数字入栈
        stack = []
        # * 上一个遇到的运算符
        # * 预置为 + 是为了能让第一个 curNum 顺利地入栈，因为 prevOp 为 + 才能触发 curNum 入栈
        prevOp = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curNum = curNum * 10 + int(char)

            if char in ["+", "-", "*", "/"] or i == len(s) - 1:
                if prevOp == "+":
                    stack.append(curNum)
                elif prevOp == "-":
                    stack.append(-curNum)
                elif prevOp == "*":
                    preNum = stack.pop()
                    productRes = preNum * curNum
                    stack.append(productRes)
                elif prevOp == "/":
                    preNum = stack.pop()
                    if preNum < 0:
                        stack.append(int(preNum / curNum))
                    else:
                        stack.append(preNum // curNum)

                prevOp = char
                curNum = 0
            print(
                f"curChar is {char}, curNum is {curNum}, preop is {prevOp}, stack is {stack}")
        res = 0
        for num in stack:
            res += num

        return res


Solution().calculate(s="3+2*2")
